"""Setup platform that offers a fake select entity."""
from __future__ import annotations

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import DEVICE_DEFAULT_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN
import requests
from . import sensor #to import ip value

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the Select entity."""
    async_add_entities(
        [
            ModeSelect(
                unique_id="smartevse_mode",
                name="SmartEVSE Mode",
                icon="mdi:power",
                current_option="SMART",
                options=[
                    "OFF",
                    "NORMAL",
                    "SOLAR",
                    "SMART",
                ],
                translation_key="mode",
            ),
        ]
    )


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Demo config entry."""
    await async_setup_platform(hass, {}, async_add_entities)


class ModeSelect(SelectEntity):
    """Representation of select entity."""

    _attr_should_poll = False #TODO not sure about this

    def __init__(
        self,
        unique_id: str,
        name: str,
        icon: str,
        current_option: str | None,
        options: list[str],
        translation_key: str,
    ) -> None:
        """Initialize the Demo select entity."""
        self._attr_unique_id = unique_id
        self._attr_name = name or DEVICE_DEFAULT_NAME
        self._attr_current_option = current_option
        self._attr_icon = icon
        self._attr_options = options
        self._attr_translation_key = translation_key
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, unique_id)},
            name=name,
        )

    async def async_select_option(self, option: str) -> None:
        """Update the current selected option."""
        self._attr_current_option = option
        self.async_write_ha_state()
