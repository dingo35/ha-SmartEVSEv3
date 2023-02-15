# ha-SmartEVSEv3

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)

SmartEVSEv3 connection for Home Assistant

## Installation using HACS (recommended)

1. Install [HACS](https://hacs.xyz/docs/setup/download) if you have that not already running; you'd want it 
		installed anyways to have access to all those wonderful custom_components....
2. From the main menu, select Hacs, select Integrations; enter "smartevse" in the search box, follow instructions to download.
3. After successful download, from the main menu, select Settings, select Devices & Services (or wherever "Integrations" are mentioned).
4. Select "add integration", enter "smartevse", and from then on follow instructions.

The main advantage of this installation method is that HomeAssistant will inform you of updates.

## Alternative install

1. Copy the folder ```custom_components/smartevse/``` to your homeassistant config directory.
2. Restart Home Assistant, and, very important and often forgotten, RESTART YOUR BROWSER!

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
		ping SmartEVSE-xxxx.local where xxxx is the serial number of your device.

2. This will only work if your SmartEVSE device is 
	- a version 3 device, 
	- running version 1.5.2 or higher from the serkri firmware (https://github.com/serkri/SmartEVSE-3/releases), 
   	The original firmware has no rest-API implemented, and does not announce itself on the mDNS network, so that will not work.
