from __future__ import annotations

import logging
from types import MappingProxyType
from typing import Any

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import SmartEVSE
from .const import DOMAIN, SELECTS
from .models import SmartEVSESelectEntityDescription
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

    for description in SELECTS:
        entities.append(SmartEVSESelect(description, client, data))

    async_add_entities(entities, True)


class SmartEVSESelect(SmartEVSEEntity, SelectEntity):
    """Representation of a SmartEVSESwitch entity."""

    entity_description: SmartEVSESelectEntityDescription

    def __init__(
        self,
        entity_description: SmartEVSESelectEntityDescription,
        client: SmartEVSE,
        data: MappingProxyType[str, Any],
    ) -> None:
        """Init SmartEVSE Switch."""
        super().__init__(entity_description, client, data)

        if self.entity_description.options is not None:
            self._attr_options = list(self.entity_description.options.values())

    @property
    def current_option(self) -> str | None:
        """Return the state of the entity."""
        if self.coordinator.data == None:
            return None
        option = self.coordinator.data.get(self.entity_description.key)
        if option is not None and self.entity_description.options is not None:
            return str(self.entity_description.options[option])
        return None

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        option_dict = self.entity_description.options
        if option_dict is not None:
            value = list(option_dict.keys())[list(option_dict.values()).index(option)]
            self.api_url = "http://" + self._client.host + "/settings?mode=" + str(value)
            await self.hass.async_add_executor_job(self.write)

    def write(self):
        res = requests.post(self.api_url, {})
        if (res == "<Response [200]>"):
            self._attr_current_option = option
            self.async_write_ha_state()
