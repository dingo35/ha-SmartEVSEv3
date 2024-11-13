"""Constants for the smartevse component."""
from __future__ import annotations
from homeassistant.const import (
    UnitOfElectricCurrent, 
    UnitOfEnergy, 
    UnitOfPower, 
    UnitOfTemperature,
    UnitOfTime,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
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
    SmartEVSESelectEntityDescription(
        key="smartevse_enable_C2",
        name="SmartEVSE C2 selector",
        options={
            "Not present": "Not present",
            "Always Off": "Always Off",
            "Solar Off": "Solar Off",
            "Always On": "Always On",
            "Auto": "Auto",
        },
        entity_registry_enabled_default=True,
    ),
)

SENSORS: tuple[SmartEVSESensorEntityDescription, ...] = (
    SmartEVSESensorEntityDescription(
        key="smartevse_fw_version",
        name="SmartEVSE Firmware version",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_serialnr",
        name="SmartEVSE Serial nr",
    ),
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
        key="smartevse_wifi_status",
        name="SmartEVSE Wifi Status",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_wifi_ssid",
        name="SmartEVSE Wifi SSID",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_wifi_rssi",
        name="SmartEVSE Wifi RSSI",
        state_class=SensorStateClass.MEASUREMENT,
        unit=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
        device_class=SensorDeviceClass.SIGNAL_STRENGTH,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_wifi_bssid",
        name="SmartEVSE Wifi BSSID",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_temp",
        name="SmartEVSE Temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
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
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_current_min",
        name="SmartEVSE Current Min",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_current_max",
        name="SmartEVSE Current Max",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_current_main",
        name="SmartEVSE Current Main",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_current_max_circuit",
        name="SmartEVSE Current MaxCircuit",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_loadbl",
        name="SmartEVSE LoadBl",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_solar_stop_time",
        name="SmartEVSE Solar Stop Time",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_home_battery_current",
        name="SmartEVSE Home Battery Current",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_home_battery_last_update",
        name="SmartEVSE Home Battery Last Update",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_ev_import_active_energy",
        name="SmartEVSE EV Import Active Energy",
        unit=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_ev_export_active_energy",
        name="SmartEVSE EV Export Active Energy",
        unit=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_ev_import_active_power",
        name="SmartEVSE EV Import Active Power",
        unit=UnitOfPower.KILO_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_ev_total_kwh",
        name="SmartEVSE EV Total kWh",
        unit=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_ev_charged_kwh",
        name="SmartEVSE EV Charged kWh",
        unit=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_ev_total",
        name="SmartEVSE EV Total",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_ev_l1",
        name="SmartEVSE EV L1",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_ev_l2",
        name="SmartEVSE EV L2",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_ev_l3",
        name="SmartEVSE EV L3",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_mains_import_active_energy",
        name="SmartEVSE Mains Import Active Energy",
        unit=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_mains_export_active_energy",
        name="SmartEVSE Mains Export Active Energy",
        unit=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_total",
        name="SmartEVSE Total Mains",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_l1",
        name="SmartEVSE Mains L1",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_l2",
        name="SmartEVSE Mains L2",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_l3",
        name="SmartEVSE Mains L3",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_mains_meter",
        name="SmartEVSE Mains Meter",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_last_data_update",
        name="SmartEVSE Last Data Update",
    ),
    SmartEVSESensorEntityDescription(
        key="smartevse_starttime",
        name="SmartEVSE StartTime",
    ),
)

SWITCHES: tuple[SmartEVSESwitchEntityDescription, ...] = (
    SmartEVSESwitchEntityDescription(
        key="smartevse_mode_switch",
        name="SmartEVSE Power",
        icon="mdi:power",
        entity_registry_enabled_default=True,
    ),
)

# TODO units should be in 10ths of Ampere
# native_min_value should be limited to MinCurrent
# native_max_value should be limited to MaxCurrent

NUMBERS: tuple[SmartEVSENumberEntityDescription, ...] = (
    SmartEVSENumberEntityDescription(
        key="smartevse_override_current",
        name="SmartEVSE Override Current",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        native_min_value=6,
        native_max_value=16,
        native_step=0.1,
        entity_registry_enabled_default=True,
    ),
    SmartEVSENumberEntityDescription(
        key="smartevse_current_max_sum_mains",
        name="SmartEVSE Grid Capacity Current",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        native_min_value=1,
        native_max_value=600,
        native_step=1,
        entity_registry_enabled_default=True,
    ),    
    SmartEVSENumberEntityDescription(
        key="smartevse_solar_max_import",
        name="SmartEVSE Solar Max Import",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        native_min_value=0,
        native_max_value=20,
        native_step=1,
        entity_registry_enabled_default=True,
    ),
    SmartEVSENumberEntityDescription(
        key="smartevse_solar_start_current",
        name="SmartEVSE Solar Start Current",
        unit=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        native_min_value=0,
        native_max_value=48,
        native_step=1,
        entity_registry_enabled_default=True,
    ),
    SmartEVSENumberEntityDescription(
        key="smartevse_solar_stop_time",
        name="Solar Stop Time",
        unit=UnitOfTime.MINUTES,
        #device_class=SensorDeviceClass.TIME,
        native_min_value=0,
        native_max_value=60,
        native_step=1,
        entity_registry_enabled_default=True,
    ),
)
