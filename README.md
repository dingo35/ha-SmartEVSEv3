# ha-SmartEVSEv3

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)

SmartEVSEv3 connection for Home Assistant

## Installation

1. Copy the folder ```custom_components/smartevse/``` to your homeassistant config directory.
2. Restart Home Assistant.

## Alternative install using HACS

Hopefully soon:
[HACS](https://hacs.xyz/) > Integrations > Plus > **SmartEVSE**

## Configuration
After installation and restart your SmartEVSE device should be discovered.
If not:
1. Go to Settings
2. Go to Integrations
3. At the bottom right, click Add Integration
4. Search for "smartevse-3"
5. Fill in your 4 digit serial number (if the integration didn't find your SmartEVSE-v3 already!)
6. Save

## Known issues
1. Your SmartEVSE device needs to be pingable by mDNS:
		ping SmartEVSE-xxxxx.local where xxxxx is the serial number of your device; 
		(this is the same serial number that the AP has in its SSID when in Wifi setup).

2. This will only work if your SmartEVSE device is 
	- a version 3 device, 
	- running version 1.5.2 or higher from the serkri firmware (https://github.com/serkri/SmartEVSE-3/releases), 
   	The original firmware has no rest-API implemented, and does not announce itself on the mDNS network, so that will not work.
