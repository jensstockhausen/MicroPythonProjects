# Template

## Files

* flash.sh: uses mpfshell to upload all files to the ESP.
* boot.py: plain boot using wifi.py to connect to the Wifi.
* main.py: connects to MQTT brocker, sets up callback for incoming messages, reads sensor and publishes message.

* wifi.py: read credentials from wifi.dat and connects to network.
* umqttsimple.py: MQTT client to connect to brocker.
* bme280_float.py: read BME280 sensor data via SPI.


## Notes

* add a wifi.dat file containing the SSID and passsord to the Wifi to connect to.
* change the password in webrepl_cfg.py for safty.
