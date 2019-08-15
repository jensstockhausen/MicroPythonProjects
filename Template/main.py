import time

# required for the BME208
from machine import I2C, Pin, unique_id, reset
from bme280_float import *

# connection on a NodeMCU ESP8266
# BME280  - SPIs
# D1 - 05 - SCL
# D2 - 04 - SDA


# reuqire for the MQTT
import ubinascii
from umqttsimple import MQTTClient

# MQTT configuration
# adjust for your configuration
mqtt_server = '192.168.3.115'

# init MQTT
client_id = ubinascii.hexlify(unique_id())
print("mqtt client id {}".format(client_id))

# init sensor
i2c = I2C(scl=Pin(5), sda=Pin(4))
bme280 = BME280(i2c=i2c, mode=BME280_OSAMPLE_2)

# callback for subscritions
def sub_cb(topic, msg):
  print((topic, msg))


def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  
  # subscribe to topics
  #client.subscribe(topic_sub)
  
  print("Connected to {} MQTT broker".format(mqtt_server))
  return client

def restart_and_reconnect():
  print("Failed to connect to MQTT broker. Reconnecting...")
  time.sleep(10)
  reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    # handle incomming messages
    # (calls sub_cb() function)
    client.check_msg()
    
    # read data from sensor
    data = bme280.read_compensated_data()
    temp = data[0] 
    dew = bme280.dew_point
    print("{}°C {}hPa {}% {}°C(dew)".format(temp, data[1], data[2], dew))
    
    #publish via mqtt
    client.publish(b'weather/room/temperature', '{:.2f}'.format(temp))
    client.publish(b'weather/room/pressure', '{:.2f}'.format(data[1]))
    client.publish(b'weather/room/humidity', '{:.2f}'.format(data[2]))
    client.publish(b'weather/room/dewpoint', '{:.2f}'.format(dew))
 
    #read in 2 minutes interval
    time.sleep(2*60)

  except OSError as e:
    restart_and_reconnect()
    
    
    