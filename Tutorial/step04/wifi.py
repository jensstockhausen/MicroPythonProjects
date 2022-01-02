import time
import network
from machine import Pin

NETWORK_PROFILES = 'wifi.dat'

def _read_profiles():
    with open(NETWORK_PROFILES) as f:
        lines = f.readlines()
    for line in lines:
        ssid, password = line.strip("\n").split(";")
    return [ssid, password]


def connect_wifi():
    
    # disable access point
    ap = network.WLAN(network.AP_IF)
    ap.active(False)

    station = network.WLAN(network.STA_IF)
    station.active(True)
    
    ssid, password = _read_profiles()
    
    #print("connecting to: {} with {}".format(ssid, password))
    print("connecting to: {}".format(ssid))
    station.connect(ssid, password)

    while station.isconnected() == False:
      time.sleep(0.5)
      print('.', end='')
      pass

    print('Connection successful')
    print(station.ifconfig())

    led = Pin(2, Pin.OUT)
    for i in range(3):
        led.off()
        time.sleep(0.2)
        led.on()
        time.sleep(0.2)

    return station.isconnected()


