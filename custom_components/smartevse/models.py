"""Models for the integration."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from homeassistant.components.number import NumberEntityDescription
from homeassistant.components.select import SelectEntityDescription
from homeassistant.components.sensor import SensorEntityDescription
from homeassistant.components.switch import SwitchEntityDescription
from homeassistant.helpers.entity import EntityDescription


@dataclass
class SmartEVSEEntityDescription(EntityDescription):
    """Represents an entity."""

    url: str | None = None
    short: str | None = None
    unit: str | None = None


@dataclass
class SmartEVSESwitchEntityDescription(SmartEVSEEntityDescription, SwitchEntityDescription):
    """Represents a switch."""


@dataclass
class SmartEVSESelectEntityDescription(SmartEVSEEntityDescription, SelectEntityDescription):
    """Represents a Select."""

    options: dict[int, Any] | None = None


@dataclass
class SmartEVSESensorEntityDescription(SmartEVSEEntityDescription, SensorEntityDescription):
    """Represents a Sensor."""


@dataclass
class SmartEVSENumberEntityDescription(SmartEVSEEntityDescription, NumberEntityDescription):
    """Represents a Number."""

    native_min_value: float | None = None
    native_max_value: float | None = None
    native_step: float | None = None
