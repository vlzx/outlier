import geoip2.database

from util import resource_path


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__INSTANCE = None

    def __call__(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__INSTANCE


class GeoIP(metaclass=Singleton):
    def __init__(self):
        self.reader = geoip2.database.Reader(resource_path('GeoLite2-Country.mmdb'))

    def country(self, ip: str) -> str:
        data = self.reader.country(ip)
        return data.country.iso_code


if __name__ == '__main__':
    t1 = GeoIP()
    t2 = GeoIP()

    print(id(t1), id(t2))
    print(t1.country('223.5.5.5'))
    print(t2.country('8.8.8.8'))
