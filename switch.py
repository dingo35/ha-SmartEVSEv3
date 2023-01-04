"""Platform for switch integration."""
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

from . import sensor

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    global name
    global serial_number
    add_entities([smartevse_mode_switch()])

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
        res = os.system("curl -s -X POST http://" + sensor.ip + "/settings?mode=3 -H 'accept: application/json' -H 'Content-Type: application/json' -d '{}'")
        self._is_on = True

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        res = os.system("curl -s -X POST http://" + sensor.ip + "/settings?mode=0 -H 'accept: application/json' -H 'Content-Type: application/json' -d '{}'")
        self._is_on = False

    def update(self) -> None:
        self.mode_id = sensor.poll.get(True)['mode_id']
        if (self.mode_id == 0):
            self._is_on = False
        else:
            self._is_on = True
