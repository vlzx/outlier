import win32event
import win32serviceutil


class Svc(win32serviceutil.ServiceFramework):
    _svc_name_ = 'Outlier'
    _svc_display_name_ = 'Outlier'
    _svc_description_ = 'HTTP转SOCKS5代理 / GeoIP分流'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
        self.entry()

    def SvcStop(self):
        self.exit()

    def entry(self):
        pass

    def exit(self):
        pass
