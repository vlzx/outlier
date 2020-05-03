from threading import Lock

import geoip2.database

from util import resource_path


class SingletonMeta(type):
    _instance = None
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls._instance


class GeoIP(metaclass=SingletonMeta):
    def __init__(self):
        self.reader = geoip2.database.Reader(resource_path('GeoLite2-Country.mmdb'))

    def country(self, ip: str) -> str:
        data = self.reader.country(ip)
        return data.country.iso_code
