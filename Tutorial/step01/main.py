import time
from machine import I2C, Pin
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
    return [data[0], data[1], data[2], dew]
        
while (True):
    read_data(bme280)
    time.sleep(2)
    