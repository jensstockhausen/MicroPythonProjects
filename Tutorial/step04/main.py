# template for MQTT client
import ubinascii
from machine import unique_id, I2C, Pin
import time
from utime import ticks_ms
from umqttsimple import MQTTClient
from bme280_float import BME280, BME280_OSAMPLE_8

# BME280 - SPIs
# D1 - 05 - SCL
# D2 - 04 - SDA



# init sensor
i2c = I2C(scl=Pin(5), sda=Pin(4))
bme280 = BME280(i2c=i2c, mode=BME280_OSAMPLE_8)


def read_data(bme280):
    data = bme280.read_compensated_data()
    dew = bme280.dew_point    
    print("{:6.2}°C {:10}hPa {:5.2}% {:6.2}°C(dew)".format(data[0], data[1], data[2], dew))
    return data[0], data[1], data[2], dew
    

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
        
    temp, press, humi, dew = read_data(bme280)
        
    print("Do publish message")
    client.publish(topic="client/{}/uptime".format(CLIENT_ID),
                   msg='{}'.format(ticks_ms()), retain=True)
    
    client.publish(topic="ambient/room/temp",
                   msg="{}".format(temp), retain=True)

    client.publish(topic="ambient/room/humidity",
                   msg="{}".format(humi), retain=True)

    #read in 2 minutes interval
    time.sleep(2*60)
    #time.sleep(5)

  except OSError as e:
    restart_and_reconnect()

