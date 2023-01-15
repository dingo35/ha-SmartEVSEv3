"""Constants for the smartevse component."""
from __future__ import annotations
from homeassistant.const import TEMP_CELSIUS, ELECTRIC_CURRENT_AMPERE, ENERGY_KILO_WATT_HOUR

from homeassistant.components.sensor import (
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    PERCENTAGE,
    PRESSURE_BAR,
    TEMP_CELSIUS,
    VOLUME_CUBIC_METERS,
)

from .models import (
    SmartEVSENumberEntityDescription,
    SmartEVSESelectEntityDescription,
    SmartEVSESensorEntityDescription,
    SmartEVSESwitchEntityDescription,
)

DOMAIN = "smartevse"

CONF_DEVICES = "devices"
CONF_SERIAL = "serial"
CONF_NAME = "name"
CONF_SWITCHES = "switches"
CONF_SENSORS = "sensors"
CONF_HOST = "host"

UPDATE_INTERVAL = 60 #in seconds

name = "name"
url = "url"
unit = "unit"
device_class = "device_class"
short = "short"
icon = "icon"
options = "options"

SELECTS: tuple[SmartEVSESelectEntityDescription, ...] = (
    SmartEVSESelectEntityDescription(
        key="smartevse_mode_id",
        name="SmartEVSE Mode selector",
        icon="mdi:power",
        options={
            0: "OFF",
            1: "NORMAL",
            2: "SOLAR",
            3: "SMART",
        },
        entity_registry_enabled_default=True,
    ),
)

SENSORS: tuple[SmartEVSESensorEntityDescription, ...] = (
    SmartEVSESensorEntityDescription(
        key="smartevse_mode",
        name="SmartEVSE Mode",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_mode_id",
        name="SmartEVSE Mode_id",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_car_connected",
        name="SmartEVSE Car Connected",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_temp",
        name="SmartEVSE Temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        unit=TEMP_CELSIUS,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_access",
        name="SmartEVSE Access",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_mode2",
        name="SmartEVSE Mode2",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_solar_stop_timer",
        name="SmartEVSE Solar Stop Timer",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_state",
        name="SmartEVSE State",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_state_id",
        name="SmartEVSE State_id",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_error",
        name="SmartEVSE Error",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_error_id",
        name="SmartEVSE Error_id",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_charge_current",
        name="SmartEVSE Charge Current",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_override_current",
        name="SmartEVSE Override Current",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_current_min",
        name="SmartEVSE Current Min",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_current_max",
        name="SmartEVSE Current Max",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_current_main",
        name="SmartEVSE Current Main",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_solar_max_import",
        name="SmartEVSE Solar Max Import",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_solar_start_current",
        name="SmartEVSE Solar Start Current",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_solar_stop_time",
        name="SmartEVSE Solar Stop Time",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_ev_import_active_energy",
        name="SmartEVSE EV Import Active Energy",
        unit=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_mains_import_active_energy",
        name="SmartEVSE Mains Import Active Energy",
        unit=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_mains_export_active_energy",
        name="SmartEVSE Mains Export Active Energy",
        unit=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_total",
        name="SmartEVSE Total Mains",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_l1",
        name="SmartEVSE Mains L1",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_l2",
        name="SmartEVSE Mains L2",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_l3",
        name="SmartEVSE Mains L3",
        unit=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_last_data_update",
        name="SmartEVSE Last Data Update",
    ),
)
