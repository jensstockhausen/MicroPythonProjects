import time
from machine import I2C, Pin, unique_id, reset
import ubinascii
from umqttsimple import MQTTClient
from bme280_float import *

# BME280 - SPIs
# D1 - 05 - SCL
# D2 - 04 - SDA

# MQTT configuration
mqtt_server = '192.168.3.115'

# init MQTT
client_id = ubinascii.hexlify(unique_id())
print("mqtt client id {}".format(client_id))

# init sensor
i2c = I2C(scl=Pin(5), sda=Pin(4))
bme280 = BME280(i2c=i2c, mode=BME280_OSAMPLE_2)

# subscritions
def sub_cb(topic, msg):
  print((topic, msg))

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  #client.subscribe(topic_sub)
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    
    data = bme280.read_compensated_data()
    
    temp = data[0] #- 4.5 # manual calibration
    
    dew = bme280.dew_point
    
    print("{}°C {}hPa {}% {}°C(dew)".format(temp, data[1], data[2], dew))
    
    client.publish(b'weather/anna/temperature', '{:.2f}'.format(temp))
    client.publish(b'weather/anna/pressure', '{:.2f}'.format(data[1]))
    client.publish(b'weather/anna/humidity', '{:.2f}'.format(data[2]))
    client.publish(b'weather/anna/dewpoint', '{:.2f}'.format(dew))
 
    #read in 2 minutes interval
    time.sleep(2*60)

  except OSError as e:
    restart_and_reconnect()
    
    
    