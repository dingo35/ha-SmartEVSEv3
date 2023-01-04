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
#    add_entities([smartevse_charging_rate()])
#    add_entities([smartevse_charging_time()])
#    add_entities([smartevse_charging_time_uitgesteld()])
    add_entities([smartevse_mode()])
    add_entities([smartevse_mode_id()])
    add_entities([smartevse_car_connected()])
    add_entities([smartevse_temp()])
    add_entities([smartevse_access()])
    add_entities([smartevse_mode2()])
    add_entities([smartevse_solar_stop_timer()])
    add_entities([smartevse_state()])
    add_entities([smartevse_state_id()])
    add_entities([smartevse_error()])
    add_entities([smartevse_error_id()])
    add_entities([smartevse_charge_current()])
    add_entities([smartevse_override_current()])
    add_entities([smartevse_current_min()])
    add_entities([smartevse_current_max()])
    add_entities([smartevse_current_main()])
    add_entities([smartevse_solar_max_import()])
    add_entities([smartevse_solar_start_current()])
    add_entities([smartevse_solar_stop_time()])
    add_entities([smartevse_ev_import_active_energy()])
    add_entities([smartevse_mains_import_active_energy()])
    add_entities([smartevse_mains_export_active_energy()])
    add_entities([smartevse_total()])
    add_entities([smartevse_l1()])
    add_entities([smartevse_l2()])
    add_entities([smartevse_l3()])
    add_entities([smartevse_last_data_update()])

    devices = get_devices()
    for device in devices:
        name = device[0].replace("._http._tcp.local.", "")
        serial_number = device[0].replace("._http._tcp.local.", "").replace("SmartEVSE-", "")
        ip=device[1]
        print("Name: %s, IP:%s, serial:%s." % (name,ip,serial_number))

class poll_API(object):
    def __init__(self):
        self.last_poll = ''
    def get(self, force = False):
        now = time.time()
        #if self.last_poll != '':
            #print(now - self.last_poll)
        if (force) or (self.last_poll == '') or (now - self.last_poll > 60) :
            print("DINGO: bothering SmartEVSE @ %s for new data!" % (ip))
            print(datetime.datetime.fromtimestamp(now))
            api_url = "http://" + ip + "/settings"
            self.response = requests.get(api_url)
            self.last_poll = now
        return self.response.json()

poll = poll_API() #TODO now we only handle 1 smartevse device on the LAN, find out how to bundle the entities into a hass device!

#    - name: smartevse_charging_rate
#      unit_of_measurement: "km/h"
#      #device_class: current
#    _attr_state_class = SensorStateClass.MEASUREMENT
#        {% if  states('sensor.smartevse_state')  == "Charging"  %}
#          {{ (3.97 * states('sensor.smartevse_charge_current') | float(0) )| round(0) }} 
#        {% else %}
#          {{ 0 }} 
#        {% endif %}
#    - name: smartevse_charging_time
#    _attr_native_unit_of_measurement = TIME_MINUTES
#      #device_class: current
#    _attr_state_class = SensorStateClass.MEASUREMENT
#        {% if  states('sensor.smartevse_state')  == "Charging"  %}
#          {{ (((states('input_number.gewenste_range') | float(0) - states('sensor.enyaq_electric_range') | float(0) )  / states('sensor.smartevse_charging_rate') | float(0)) * 60 ) | round(0) }} 
#        {% else %}
#          {{ 0 }} 
#        {% endif %}
#    - name: smartevse_charging_time_uitgesteld
#    _attr_native_unit_of_measurement = TIME_MINUTES
#      #device_class: current
#    _attr_state_class = SensorStateClass.MEASUREMENT
#        {% if  states('sensor.smartevse_state')  == "Charging"  %}
#          {{ (((states('input_number.gewenste_range_uitgesteld_laden') | float(0) - states('sensor.enyaq_electric_range') | float(0) )  / states('sensor.smartevse_charging_rate') | float(0)) * 60 ) | round(0) }} 
#        {% else %}
#          {{ 0 }} 
#        {% endif %}
class smartevse_mode(SensorEntity):
    _attr_name = "smartevse_mode"
    def update(self) -> None:
        self._attr_native_value = poll.get()['mode']
class smartevse_mode_id(SensorEntity):
    _attr_name = "smartevse_mode_id"
    def update(self) -> None:
        self._attr_native_value = poll.get()['mode_id']
class smartevse_car_connected(SensorEntity):
    _attr_name = "smartevse_car_connected"
    def update(self) -> None:
        self._attr_native_value = poll.get()['car_connected']
class smartevse_temp(SensorEntity):
    _attr_name = "smartevse_temp"
    def update(self) -> None:
        self._attr_native_value = poll.get()['evse']['temp']
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_native_unit_of_measurement = TEMP_CELSIUS
class smartevse_access(SensorEntity):
    _attr_name = "smartevse_access"
    def update(self) -> None:
        self._attr_native_value = poll.get()['evse']['access']
class smartevse_mode2(SensorEntity):
    _attr_name = "smartevse_mode2"
    def update(self) -> None:
        self._attr_native_value = poll.get()['evse']['mode']
class smartevse_solar_stop_timer(SensorEntity):
    _attr_name = "smartevse_solar_stop_timer"
    def update(self) -> None:
        self._attr_native_value = poll.get()['evse']['solar_stop_timer']
class smartevse_state(SensorEntity):
    _attr_name = "smartevse_state"
    def update(self) -> None:
        self._attr_native_value = poll.get()['evse']['state']
class smartevse_state_id(SensorEntity):
    _attr_name = "smartevse_state_id"
    def update(self) -> None:
        self._attr_native_value = poll.get()['evse']['state_id']
class smartevse_error(SensorEntity):
    _attr_name = "smartevse_error"
    def update(self) -> None:
        self._attr_native_value = poll.get()['evse']['error']
class smartevse_error_id(SensorEntity):
    _attr_name = "smartevse_error_id"
    def update(self) -> None:
        self._attr_native_value = poll.get()['evse']['error_id']
class smartevse_charge_current(SensorEntity):
    _attr_name = "smartevse_charge_current"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['settings']['charge_current'] / 10
class smartevse_override_current(SensorEntity):
    _attr_name = "smartevse_override_current"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['settings']['override_current']
class smartevse_current_min(SensorEntity):
    _attr_name = "smartevse_current_min"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['settings']['current_min']
class smartevse_current_max(SensorEntity):
    _attr_name = "smartevse_current_max"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['settings']['current_max']
class smartevse_current_main(SensorEntity):
    _attr_name = "smartevse_current_main"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['settings']['current_main']
class smartevse_solar_max_import(SensorEntity):
    _attr_name = "smartevse_solar_max_import"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['settings']['solar_max_import']
class smartevse_solar_start_current(SensorEntity):
    _attr_name = "smartevse_solar_start_current"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['settings']['solar_start_current']
class smartevse_solar_stop_time(SensorEntity):
    _attr_name = "smartevse_solar_stop_time"
    def update(self) -> None:
        self._attr_native_value = poll.get()['settings']['solar_stop_time']
class smartevse_ev_import_active_energy(SensorEntity):
    _attr_name = "smartevse_ev_import_active_energy"
    _attr_native_unit_of_measurement = ENERGY_KILO_WATT_HOUR
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL
    def update(self) -> None:
        self._attr_native_value = poll.get()['ev_meter']['import_active_energy']
class smartevse_mains_import_active_energy(SensorEntity):
    _attr_name = "smartevse_mains_import_active_energy"
    _attr_native_unit_of_measurement = ENERGY_KILO_WATT_HOUR
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL
    def update(self) -> None:
        self._attr_native_value = poll.get()['mains_meter']['import_active_energy']
class smartevse_mains_export_active_energy(SensorEntity):
    _attr_name = "smartevse_mains_export_active_energy"
    _attr_native_unit_of_measurement = ENERGY_KILO_WATT_HOUR
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL
    def update(self) -> None:
        self._attr_native_value = poll.get()['mains_meter']['export_active_energy']
class smartevse_total(SensorEntity):
    _attr_name = "smartevse_total"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['phase_currents']['TOTAL'] / 10
class smartevse_l1(SensorEntity):
    _attr_name = "smartevse_l1"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['phase_currents']['L1'] / 10
class smartevse_l2(SensorEntity):
    _attr_name = "smartevse_l2"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['phase_currents']['L2'] / 10
class smartevse_l3(SensorEntity):
    _attr_name = "smartevse_l3"
    _attr_native_unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    _attr_device_class = SensorDeviceClass.CURRENT
    def update(self) -> None:
        self._attr_native_value = poll.get()['phase_currents']['L3'] / 10
class smartevse_last_data_update(SensorEntity):
    _attr_name = "smartevse_last_data_update"
    def update(self) -> None:
        self._attr_native_value = datetime.datetime.fromtimestamp(poll.get()['phase_currents']['last_data_update'])
