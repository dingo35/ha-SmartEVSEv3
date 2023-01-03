#generates list of smartevses and their ip addresses on the network
from zeroconf import ServiceBrowser, Zeroconf
import time

class MyListener:

    devices = []

    def update_service(self, zeroconf, type, name):
        #dummy line
        tmp = 0

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info: 
            #if name.startswith(""):
            if name.startswith("SmartEVSE"):
                self.device = []
                self.device.append(name)
                self.device.append(info.parsed_addresses()[0])
                self.devices.append(self.device)

def get_devices():
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    time.sleep(8)
    zeroconf.close()
    return listener.devices

def main():
    #devices = get_devices()
    print("Found devices:%s." % (get_devices()))

if __name__ == "__main__":
    main()
