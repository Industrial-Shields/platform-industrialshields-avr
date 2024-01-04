# Industrial Shields Arduino PLCs: development platform for [PlatformIO](https://platformio.org)

This repository contains the configurations and examples to use the PlatformIO ecosystem with our Industrial Shields PLCs based on Arduino open-source hardware. You can check the documentation of our Arduino-based PLCs in our [web page](https://www.industrialshields.com/industrial-plc-based-on-arduino-original-boards-automation-solutions-202209-lp).

# Usage

1. [Install PlatformIO](https://platformio.org)
2. Create a PlatformIO project and configure a platform option in the [platformio.ini](https://docs.platformio.org/page/projectconf.html) file:

``` ini
[env]
platform_packages =
   framework-industrialshields-avr@https://apps.industrialshields.com/main/arduino/boards/industrialshields-boards-avr-X.X.X.tar.bz2

[env:board]
platform = https://github.com/Industrial-Shields/platform-industrialshields-avr.git
board = ...
...
```

You can check all the available versions in https://apps.industrialshields.com/main/arduino/boards/ (all versions below 1.1.42 do NOT support PlatformIO).
