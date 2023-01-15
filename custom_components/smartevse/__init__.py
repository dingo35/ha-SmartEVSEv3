"""Support for third generation SmartEVSE from stegen.com"""
from __future__ import annotations

import asyncio
from datetime import timedelta
import logging
import re
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    CONF_SERIAL,
    CONF_HOST,
    DOMAIN,
    short,
    UPDATE_INTERVAL,
)
from .models import SmartEVSEEntityDescription
import requests
import datetime

_LOGGER = logging.getLogger(__name__)


DOMAINS = ["sensor", "select"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the SmartEVSE component."""
    hass.data.setdefault(DOMAIN, {})

    hass.data[DOMAIN][entry.entry_id] = {}

    credentials = dict(entry.data)
    client = SmartEVSE(hass, credentials)
    hass.data[DOMAIN][entry.entry_id]["client"] = client

    for domain in DOMAINS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, domain)
        )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload SmartEVSE  component."""
    if not all(
        await asyncio.gather(
            *(
                hass.config_entries.async_forward_entry_unload(entry, component)
                for component in DOMAINS
            )
        )
    ):
        return False

    client = hass.data[DOMAIN][entry.entry_id]["client"]

    #await client.shutdown("Unload entry")

    hass.data[DOMAIN].pop(entry.entry_id)

    return True


class SmartEVSE(DataUpdateCoordinator):
    """Supporting class for SmartEVSE ."""

    def __init__(self, hass: HomeAssistant, config: dict[str, Any]) -> None:
        _LOGGER.debug("Initialize SmartEVSE class")

        self._data: dict[str, Any] = {}  # stores device states and values
        self._event = asyncio.Event()
        self._lock = asyncio.Lock()
        self.hass = hass
        self.serial = config[CONF_SERIAL]
        self.host = config[CONF_HOST]
        self._config = config

        self._urls: dict[str, Any] = {}
        self._status_keys: dict[str, Any] = {}

        update_interval = timedelta(seconds=UPDATE_INTERVAL)

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=update_interval,
        )

    async def add_key(self, entity_description: SmartEVSEEntityDescription) -> None:
        """Add key to list of endpoints."""
        async with self._lock:
            if entity_description.url is not None:
                self._urls[entity_description.url] = {
                    "key": entity_description.key,
                    short: entity_description.short,
                }
            elif entity_description.short is not None:
                self._status_keys[entity_description.short] = entity_description.key

    async def _async_update_data(self) -> dict[str, Any]:
        """Update data via library."""
        self.response = await self.hass.async_add_executor_job(self.get_data)
        self._data["smartevse_mode"] = self.response['mode']
        self._data["smartevse_mode_id"] = self.response['mode_id']
        self._data["smartevse_car_connected"] = self.response['car_connected']
        self._data["smartevse_temp"] = self.response['evse']['temp']
        self._data["smartevse_access"] = self.response['evse']['access']
        self._data["smartevse_mode2"] = self.response['evse']['mode']
        self._data["smartevse_solar_stop_timer"] = self.response['evse']['solar_stop_timer']
        self._data["smartevse_state"] = self.response['evse']['state']
        self._data["smartevse_state_id"] = self.response['evse']['state_id']
        self._data["smartevse_error"] = self.response['evse']['error']
        self._data["smartevse_error_id"] = self.response['evse']['error_id']
        self._data["smartevse_charge_current"] = self.response['settings']['charge_current'] / 10
        self._data["smartevse_override_current"] = self.response['settings']['override_current']
        self._data["smartevse_current_min"] = self.response['settings']['current_min']
        self._data["smartevse_current_max"] = self.response['settings']['current_max']
        self._data["smartevse_current_main"] = self.response['settings']['current_main']
        self._data["smartevse_solar_max_import"] = self.response['settings']['solar_max_import']
        self._data["smartevse_solar_start_current"] = self.response['settings']['solar_start_current']
        self._data["smartevse_solar_stop_time"] = self.response['settings']['solar_stop_time']
        self._data["smartevse_ev_import_active_energy"] = self.response['ev_meter']['import_active_energy']
        self._data["smartevse_mains_import_active_energy"] = self.response['mains_meter']['import_active_energy']
        self._data["smartevse_mains_export_active_energy"] = self.response['mains_meter']['export_active_energy']
        self._data["smartevse_total"] = self.response['phase_currents']['TOTAL'] / 10
        self._data["smartevse_l1"] = self.response['phase_currents']['L1'] / 10
        self._data["smartevse_l2"] = self.response['phase_currents']['L2'] / 10
        self._data["smartevse_l3"] = self.response['phase_currents']['L3'] / 10
        self._data["smartevse_last_data_update"] = datetime.datetime.fromtimestamp(self.response['phase_currents']['last_data_update'])
        return self._data

    def get_data(self):
        api_url = "http://" + self.host + "/settings"
        ret = requests.get(api_url).json() #TODO error handling
        return ret

