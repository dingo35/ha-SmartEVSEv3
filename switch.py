"""Platform for sensor integration."""
from __future__ import annotations
import datetime
import time

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import TEMP_CELSIUS, ELECTRIC_CURRENT_AMPERE, ENERGY_KILO_WATT_HOUR
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

import requests

#generates list of smartevses and their ip addresses on the network
from zeroconf import ServiceBrowser, Zeroconf

DOMAIN="smartevse"
CONF_NAME="name"

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
    #zeroconf = await zeroconf.async_get_instance(hass)
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    time.sleep(8)
    zeroconf.close()
    return listener.devices

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    global ip
    global name
    global serial_number
    add_entities([smartevse_mode_switch()])

    devices = get_devices()
    for device in devices:
        name = device[0].replace("._http._tcp.local.", "")
        serial_number = device[0].replace("._http._tcp.local.", "").replace("SmartEVSE-", "")
        ip=device[1]
        print("Name: %s, IP:%s, serial:%s." % (name,ip,serial_number))

class poll_API(object):
    def __init__(self):
        self.last_poll = ''
    def get(self):
        now = time.time()
        #if self.last_poll != '':
            #print(now - self.last_poll)
        if (self.last_poll == '') or (now - self.last_poll > 60) :
            print("DINGO: bothering SmartEVSE @ %s for new data!" % (ip))
            print(datetime.datetime.fromtimestamp(now))
            api_url = "http://" + ip + "/settings"
            self.response = requests.get(api_url)
            self.last_poll = now
        return self.response.json()

poll = poll_API() #TODO now we only handle 1 smartevse device on the LAN, find out how to bundle the entities into a hass device!

import os
from homeassistant.components.switch import SwitchEntity


class smartevse_mode_switch(SwitchEntity):
    _attr_has_entity_name = True
    _attr_name = "smartevse_mode_switch"

    def __init__(self):
        self._is_on = False
#        self._attr_device_info = "Device INFO2"  # For automatic device registration
        self._attr_unique_id = "Unique ID2"
        self._attr_device_info = {
#            "identifiers": {(DOMAIN, self._config[serial_number])},
#            "name": self._config[CONF_NAME],
            "manufacturer": "Stegen",
            "name" : "SMARTEVSE NAAM"
        }


    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self._is_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        res = os.system("curl -s -X POST http://SmartEVSE-51446.lan/settings?mode=3 -H 'accept: application/json' -H 'Content-Type: application/json' -d '{}'")
        self._is_on = True

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        res = os.system("curl -s -X POST http://SmartEVSE-51446.lan/settings?mode=0 -H 'accept: application/json' -H 'Content-Type: application/json' -d '{}'")
        self._is_on = False
