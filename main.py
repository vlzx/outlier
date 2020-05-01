import socket
import sys

import win32event
import win32serviceutil
import servicemanager

from config import config
from client_handler import ClientHandler
from service import Svc


class Main(Svc):
    def entry(self):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind(('127.0.0.1', config.LISTEN_PORT))
        listener.listen()
        while True:
            client, _ = listener.accept()
            if win32event.WaitForSingleObject(self.stop_event, 1) == win32event.WAIT_OBJECT_0:
                break
            t = ClientHandler(client)
            t.start()

    def exit(self):
        # self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        stop_signal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        stop_signal.connect(('127.0.0.1', config.LISTEN_PORT))
        stop_signal.close()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.PrepareToHostSingle(Main)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(Main)

# if __name__ == '__main__':
    # listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # listener.bind(('127.0.0.1', config.LISTEN_PORT))
    # listener.listen()
    # while True:
    #     client, _ = listener.accept()
    #     t = ClientHandler(client)
    #     t.start()
