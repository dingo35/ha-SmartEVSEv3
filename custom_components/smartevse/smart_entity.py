"""Support for SmartEVSEv3 from Stegen"""

from __future__ import annotations

import logging
from types import MappingProxyType
from typing import Any

from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceInfo

from . import SmartEVSE
from .const import CONF_SERIAL, DOMAIN
from .models import SmartEVSEEntityDescription

_LOGGER = logging.getLogger(__name__)


class SmartEVSEEntity(CoordinatorEntity):
    """Representation of a SmartEVSE entity."""

    entity_description: SmartEVSEEntityDescription

    def __init__(
        self,
        entity_description: SmartEVSEEntityDescription,
        client: SmartEVSE,
        data: MappingProxyType[str, Any],
    ) -> None:
        """Initialize the sensor."""
        super().__init__(client)

        self.entity_description = entity_description

        self._client = client
        self._config = data
        self._attr_unique_id = (
            f"{self._config[CONF_SERIAL]}_{self.entity_description.key}"
        )
        self._attr_device_info = DeviceInfo(
            name="SmartEVSE-" + self._config[CONF_SERIAL],
            identifiers={(DOMAIN, self._config[CONF_SERIAL])},
            manufacturer="Stegen",
            model="SmartEVSE v3",
            configuration_url="http://" + client.host
        )

    async def async_added_to_hass(self) -> None:
        """Add required data to coordinator."""
        await self._client.add_key(self.entity_description)
        await super().async_added_to_hass()

    def get_endpoint(self) -> Any:
        """Get end point."""
        return self.entity_description.url
