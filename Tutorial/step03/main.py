# template for MQTT client
import ubinascii
from machine import unique_id
import time
from utime import ticks_ms
from umqttsimple import MQTTClient


# MQTT configuration
MQTT_SERVER = '192.168.42.1'  #where your mosquitto server is running
CLIENT_ID = ubinascii.hexlify(unique_id()).decode("utf-8") 


# callback to handle subscritions
def subscrition_callback(topic, msg):
  print("Topic: [{}] Message [{}]".format(topic, msg))


def connect_and_subscribe(CLIENT_ID, MQTT_SERVER):
  client = MQTTClient(CLIENT_ID, MQTT_SERVER)
  client.set_callback(subscrition_callback)
  
  client.connect()
  client.subscribe("client/{}/check".format(CLIENT_ID))
  
  print("Connected to MQTT broker {}".format(MQTT_SERVER))
  return client


def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  reset()


try:
  client = connect_and_subscribe(CLIENT_ID, MQTT_SERVER)
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
        
    print("Do publish message")
    client.publish(topic="client/{}/uptime".format(CLIENT_ID),
                   msg='{}'.format(ticks_ms()),
                   retain=True)

    #read in 2 minutes interval
    time.sleep(2*60)

  except OSError as e:
    restart_and_reconnect()

