from zeroconf import ServiceBrowser, Zeroconf
import time

class MyListener:

    def update_service(self, zeroconf, type, name):
        #dummy line
        tmp = 0

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info: 
            if name.startswith("SmartEVSE"):
                print("%s,%s" % (name, info.parsed_addresses()[0]))
                #zeroconf.close()
                #print("BINGO!")
            #print("Service %s added, service info: %s" % (name, info))
            #print("Service %s added, IP address: %s" % (name, socket.inet_ntoa(info.address)))


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
time.sleep(5)
zeroconf.close()
