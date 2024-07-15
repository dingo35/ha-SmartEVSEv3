# ha-SmartEVSEv3

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)

SmartEVSEv3 connection for Home Assistant

## Installation using HACS (recommended)

1. Install [HACS](https://hacs.xyz/docs/setup/download) if you have that not already running; you'd want it 
		installed anyways to have access to all those wonderful custom_components....
2. From the main menu, select HACS, select Integrations, select Explore & Download repositories; enter "smartevse" in the search box, follow instructions to download.
3. Restart Home Assistant, and, very important and often forgotten, RESTART YOUR BROWSER! Really close your browser window and reopen it. F5 is not enough!
4. After restart, from the main menu, select Settings, select Devices & Services (or wherever "Integrations" are mentioned); you will probably see your SmartEVSE installed.
    
   If not (because you don't have mDNS configured on your HomeAssistant Server, you have your SmartEVSE on a different vlan/network segment than your HomeAssistant Server, or other network mis/nonstandard configurations):
    
5. Select "add integration", enter "smartevse", and from then on follow instructions.
6. Restart Home Assistant, and, very important and often forgotten, RESTART YOUR BROWSER!

The main advantage of this installation method is that HomeAssistant will inform you of updates.

## Alternative install

1. Copy the folder ```custom_components/smartevse/``` to your homeassistant config directory.
2. From here on follow goto 3. of the above HACS Installation method.

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
1. For automatic discovery, your SmartEVSE device needs to be pingable by mDNS:
		ping SmartEVSE-xxxx.local where xxxx is the serial number of your device.

2. This will only work if your SmartEVSE device is 
	- a version 3 device, 
	- running version 1.5.2 or higher from the serkri firmware (https://github.com/serkri/SmartEVSE-3/releases);
      The serkri firmware is deprecated, from v1.8.0 on development proceeded in
      https://github.com/dingo35/SmartEVSE-3.5/releases (community, bleeding edge) and
      https://github.com/SmartEVSE/SmartEVSE-3/releases (Stegen Electronics, stable).
      Version numbering between those repo's are kept consistent.
