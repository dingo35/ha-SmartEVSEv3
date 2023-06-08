from __future__ import annotations

import logging
from types import MappingProxyType
from typing import Any

from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, NUMBERS
from .models import SmartEVSENumberEntityDescription
from .smart_entity import SmartEVSEEntity
import requests

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    entities: list[SmartEVSEEntity] = []

    client = hass.data[DOMAIN][config_entry.entry_id]["client"]
    data = config_entry.data

    for description in NUMBERS:
        entities.append(SmartEVSENumber(description, client, data))

    async_add_entities(entities, True)


class SmartEVSENumber(SmartEVSEEntity, NumberEntity):

    entity_description: SmartEVSENumberEntityDescription

    def __init__(
        self,
        entity_description: SmartEVSENumberEntityDescription,
        client: SmartEVSE,
        data: MappingProxyType[str, Any],
    ) -> None:
        super().__init__(entity_description, client, data)

        if entity_description.native_min_value is not None:
            self._attr_native_min_value = entity_description.native_min_value
        if entity_description.native_max_value is not None:
            self._attr_native_max_value = entity_description.native_max_value
        if entity_description.native_step is not None:
            self._attr_native_step = entity_description.native_step

    @property
    def native_value(self) -> float | None:
        """Return the entity value to represent the entity state."""
        #prevent error message at startup
        if (not self.coordinator.data == None):
            value = self.coordinator.data.get(self.entity_description.key)
            #TODO can this be deleted?:
            if (self.entity_description.key == "smartevse_override_current"):
                value = value
            #self.coordinator._data["smartevse_override_current"] = value

        else:
            value = None

        return value

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        """self._client.smart.put_value(self.get_endpoint(), value)"""
        if (self.entity_description.key == "smartevse_solar_stop_time"):
            self.api_url = "http://" + self._client.host + "/settings?stop_timer=" + str(value)
        elif (self.entity_description.key == "smartevse_override_current"):
            self.api_url = "http://" + self._client.host + "/settings?override_current=" + str(value * 10)
        elif (self.entity_description.key == "smartevse_solar_start_current"):
            self.api_url = "http://" + self._client.host + "/settings?solar_start_current=" + str(value)
        elif (self.entity_description.key == "smartevse_solar_max_import"):
            self.api_url = "http://" + self._client.host + "/settings?solar_max_import=" + str(value)
        await self.hass.async_add_executor_job(self.write)

    def write(self):
        res = requests.post(self.api_url, {})
        if res.status_code == 200:
            self.async_write_ha_state()

