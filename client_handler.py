import socket
import threading
from urllib.parse import urlparse
import socks

from config import config
from geoip import GeoIP


class ClientHandler(threading.Thread):
    Socket = socket.socket
    BUFFER_SIZE = 1024 * 4

    def __init__(self, client: Socket):
        super().__init__()
        self.client = client

    def run(self):
        self.handle_client()

    def handle_client(self):
        method: str
        host: str
        protocol: str
        hostname: str
        port: int

        b: bytes = self.client.recv(self.BUFFER_SIZE)
        try:
            method, host, protocol = b.strip().decode('ascii').split('\r\n')[0].split(' ')
        except ValueError:
            return

        url = urlparse(host)
        server = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
        if url.scheme == 'http':
            port = url.port if url.port else 80
            hostname = url.hostname
        else:
            hostname, port = url.path.split(':')
            port = int(port)

        country: str = ''
        try:
            country = GeoIP().country(socket.gethostbyname(hostname))
        except socket.gaierror:
            pass
        if country != 'CN':
            server.set_proxy(socks.SOCKS5, '127.0.0.1', config.PROXY_PORT)

        try:
            server.connect((hostname, port))
        except (OSError, ConnectionError, TimeoutError):
            self.client.close()
            server.close()
            return

        if method == 'CONNECT':
            self.client.send(f'{protocol} 200 Connection established\r\n\r\n'.encode('ascii'))
        else:
            server.send(b)

        t = threading.Thread(target=lambda: self.copy(self.client, server))
        t.start()

        self.copy(server, self.client)

    def copy(self, src: Socket, dst: Socket):
        buffer: bytes
        try:
            while True:
                buffer = src.recv(self.BUFFER_SIZE)
                if len(buffer) <= 0:
                    break
                dst.send(buffer)
        except (OSError, ConnectionError, TimeoutError):
            pass
        finally:
            src.close()
            # dst.close()
