"""Platform for switch integration."""
from __future__ import annotations

from homeassistant.components.switch import SwitchEntity
import requests
from . import sensor

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the switch platform."""
    add_entities([smartevse_mode_switch()])


class smartevse_mode_switch(SwitchEntity):
    _attr_has_entity_name = True
    _attr_name = "smartevse_mode_switch"

    def __init__(self):
        self._is_on = False
        self._attr_unique_id = "Unique ID2"
        self._attr_device_info = {
            "manufacturer": "Stegen",
            "name" : "SmartEVSEv3"
        }

    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self._is_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        api_url = "http://" + sensor.ip + "/settings?mode=3"
        res = requests.post(api_url, {})
        if (res == "<Response [200]>"):
            self._is_on = True

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        api_url = "http://" + sensor.ip + "/settings?mode=0"
        res = requests.post(api_url, {})
        if (res == "<Response [200]>"):
            self._is_on = False

    def update(self) -> None:
        self.mode_id = sensor.poll.get(True)['mode_id']
        if (self.mode_id == 0):
            self._is_on = False
        else:
            self._is_on = True
