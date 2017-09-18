# script.kodi.zip.ambient.light

A Kodi add-on that controls ZIP (Zbenyho IoT protocol) lights.

In development, probably not working.

## Installation

The add-on requires Kodi add-on "requests".

**Kodi add-on script.module.requests**

 - download the add-on as a ZIP file from https://github.com/beenje/script.module.requests
  - (click on the green "Clone or download button" then click on the "Download ZIP" link)
 - open Kodi
 - go to `Add-ons -> click on the opened box in top left corner -> Install from zip file -> navigate to the downloaded zip file`
 - select the zip file.

**Kodi add-on script.kodi.hue.ambilight**

 - download the add-on as a ZIP file from the top of this page
  - (click on the green "Clone or download button" then click on the "Download ZIP" link)
 - go to `Add-ons -> click on the opened box in top left corner -> Install from zip file -> navigate to the downloaded zip file`
 -  restart Kodi and configure the add-on:
   - `Add-ons -> My add-ons -> Services -> Kodi Philips Hue -> Configure`
   - click `Discover Hue Bridge` and follow the instructions (press button on the Hue bridge)
   - setup the groups and tweak settings to your liking

# Note for ARM users #
## Nvidia Shield / most Android boxes ##
- _Ambilight mode_ doesn't properly work with 4k-HD codecs (>1080p) when "allow hardware acceleration - Mediacodec (Surface)" is enabled.
## Raspberry Pi's: ##
 - Save the add-on configuration by exiting Kodi before shutting down the Pi completely
 - _Ambilight mode_ might work on _Raspberry Pi's_ with most codecs and contents up to 1080p (feedback from thutterer on a RPI 3)
