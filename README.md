# MicroPython Projects


This is a collection of MicroPython projects mainly used for home automation based on ESP8222 boards using MQTT and node-red.
Please find below a list us useful links.


## Projects

### Template
A template project setting up wifi and mqtt connection.

## Links

* [MicroPython](http://micropython.org/): python for ESP boards.
* [Thonny](https://thonny.org/): IDE with MicroPython support. (try the 3.2.0 beta)

Python libraries/snippets used:
* [umqtt.simple](https://github.com/micropython/micropython-lib/tree/master/umqtt.simple): simple MQTT client 
* [bme280_float](https://github.com/robert-hh/BME280/blob/master/bme280_float.py): reading the temperature/pressure sensor BME280.

additional python packages used:
* [esptool](https://github.com/espressif/esptool): tool to flash the firmware.
* [mpfshell](https://github.com/wendlers/mpfshell): shell based file explorer to automate uploads of scripts. 

## Expanding

### ESP32
Need asecond UART? (e.g. for GPS) Think about an ESP32. 
Comes with DAC/ADC and capacitive touch sensors. 

### Visual Sudio Code & PlatformIO
More control and more frameworks.
BUT: C++ ;-)

Take [Visual Studio Code](https://code.visualstudio.com/) and install the [PlatformIO](https://platformio.org/) plugin.
It installs all required tool chains and manages libraries.





