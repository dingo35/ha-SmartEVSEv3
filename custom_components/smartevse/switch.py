from __future__ import annotations

import logging
from types import MappingProxyType
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, SWITCHES
from .models import SmartEVSESwitchEntityDescription
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

    for description in SWITCHES:
        entities.append(SmartEVSESwitch(description, client, data))

    async_add_entities(entities, True)


class SmartEVSESwitch(SmartEVSEEntity, SwitchEntity):

    entity_description: SmartEVSESwitchEntityDescription

    def __init__(
        self,
        entity_description: SmartEVSESwitchEntityDescription,
        client: SmartEVSE,
        data: MappingProxyType[str, Any],
        on_value: str = "on",
        off_value: str = "off",
    ) -> None:
        super().__init__(entity_description, client, data)

        self._on_value = on_value
        self._off_value = off_value

    @property
    def assumed_state(self) -> bool:
        """Return true if we do optimistic updates."""
        return False

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the entity on."""
        self.api_url = "http://" + self._client.host + "/settings?mode=3"
        await self.hass.async_add_executor_job(self.write)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the entity off."""
        self.api_url = "http://" + self._client.host + "/settings?mode=0"
        await self.hass.async_add_executor_job(self.write)

    def write(self):
        res = requests.post(self.api_url, {})
        if (res == "<Response [200]>"):
            self.async_write_ha_state()
