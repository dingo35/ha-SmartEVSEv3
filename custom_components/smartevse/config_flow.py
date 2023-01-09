from __future__ import annotations

import asyncio
import logging
from typing import Any

from homeassistant import config_entries, core, exceptions
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType
import voluptuous as vol

from .const import (  # pylint:disable=unused-import
    CONF_NAME,
    CONF_SERIAL,
    DOMAIN,
)
from homeassistant.components import zeroconf
from homeassistant.data_entry_flow import FlowResult

_LOGGER = logging.getLogger(__name__)

import requests

class SmartEVSEConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for SmartEVSE."""

    VERSION = 1

    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self) -> None:
        self._serial = None

    async def async_step_zeroconf(
        self, discovery_info: zeroconf.ZeroconfServiceInfo
    ) -> FlowResult:
        """Handle zeroconf discovery."""
        errors: dict[str, str] = {}

        if not discovery_info.hostname.startswith("SmartEVSE"):
            return self.async_abort(reason="invalid_mdns")

        serial_number = discovery_info.hostname.replace(".local.", "").replace(
            "SmartEVSE-", ""
        )
        await self.async_set_unique_id(serial_number)
        self._abort_if_unique_id_configured()

        # Attempt to make a connection to the local device and abort if not possible
        try:
            await self.validate_smartevse_connection(serial_number)
        except CannotConnect:
            errors["base"] = "cannot_connect"
        if not errors:
            self._serial = serial_number
            return await self.async_step_options()

    async def validate_smartevse_connection(self, serial:Str ):
        self._serial = serial
        self.response = await self.hass.async_add_executor_job(self.get_data)

    def get_data(self):
        ip = "SmartEVSE-" + self._serial + ".local"
        api_url = "http://" + ip + "/settings"
        try:
            requests.get(api_url).json() #TODO error handling
        except requests.exceptions.RequestException as e:
            raise CannotConnect("Cannot connect to url:%s" % (api_url))

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Step when user initializes an integration."""
        errors: dict[str, str] = {}
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_SERIAL])
            self._abort_if_unique_id_configured()

            try:
                await self.validate_smartevse_connection(user_input[CONF_SERIAL])
            except CannotConnect:
                errors["base"] = "cannot_connect"

            if not errors:
                self._serial = user_input[CONF_SERIAL]
                return await self.async_step_options()

        schema = vol.Schema(
            {
                vol.Required(CONF_SERIAL): cv.string,
            }
        )

        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)

    async def async_step_options(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Step to set options."""
        errors: dict[str, str] = {}
        data = {
            CONF_SERIAL: self._serial,
            CONF_NAME: "SmartEVSE",
        }

        return self.async_create_entry(title=f"{self._serial}", data=data)


class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""
