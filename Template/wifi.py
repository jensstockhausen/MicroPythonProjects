import time
import os
import network
from machine import Pin

# create this file add upload it to the ESP
# content shall be one line with
# the_ssid;the_password
NETWORK_PROFILES = 'wifi.dat'

# pin of embedded LED on board to display status
LED_PIN = 16

def _read_profiles():
    if 'wifi.dat' not in os.listdir():
        print("{} file is missing".format(NETWORK_PROFILES))
        return [None, None]
    with open(NETWORK_PROFILES) as f:
        lines = f.readlines()
    for line in lines:
        ssid, password = line.strip("\n").split(";")
    return [ssid, password]


def connect_wifi():
    led = Pin(LED_PIN, Pin.OUT)
    led.off()

    station = network.WLAN(network.STA_IF)
    station.active(True)
    
    ssid, password = _read_profiles()
    
    if ssid is None:
        return False
    
    #print("connecting to: {} with {}".format(ssid, password))
    print("connecting to: {}".format(ssid))
    station.connect(ssid, password)

    while station.isconnected() == False:
      time.sleep(0.5)
      print('.', end='')
      pass

    print('Connection successful')
    print(station.ifconfig())

    for i in range(3):
        led.off()
        time.sleep(0.2)
        led.on()
        time.sleep(0.2)

    return station.isconnected()
