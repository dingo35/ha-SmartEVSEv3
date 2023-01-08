from __future__ import annotations

from contextlib import suppress
import logging

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from .const import DOMAIN, SENSORS
from .models import SmartEVSESensorEntityDescription
from .smart_entity import SmartEVSEEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Sensor platform setup"""
    entities: list[SmartEVSEEntity] = []

    client = hass.data[DOMAIN][config_entry.entry_id]["client"]
    data = config_entry.data

    for description in SENSORS:
        entities.append(SmartEVSESensor(description, client, data))

    async_add_entities(entities, True)


class SmartEVSESensor(SmartEVSEEntity, SensorEntity):
    """Representation of a SmartEVSESensor entity."""

    entity_description: SmartEVSESensorEntityDescription

    @property
    def native_value(self) -> StateType:
        # def state(self) -> Any:
        """Return the state/value of the sensor."""

        #prevent error message at startup
        if (not self.coordinator.data == None):
            value = self.coordinator.data.get(self.entity_description.key)
        else:
            value = None

        if value is None:
            return value

        with suppress(TypeError):
            if self.device_class == SensorDeviceClass.TEMPERATURE:
                return round(float(value), 1)

        return value

    @property
    def native_unit_of_measurement(self) -> str | None:
        """Return the unit of measurement of the sensor."""
        return self.entity_description.unit
