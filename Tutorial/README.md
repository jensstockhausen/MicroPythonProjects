# Tutorial

Short walktrough to get an small ESP8266 project up and running.

Create one project and copy the files from the steps or adjust your files


## Step 1
Attach a BME280 sensor and get the readings for 
temperature, pressure etc.


## Step 2
Get a connction to the wifi to be able to communicate

**Note:** You'll have to add a `wifi.dat` file containing your 
credentials to the wifi access point your're using. 
(see comment in `wifi.py`)

## Step 3
Connect to an MQTT server via the wifi. 

**Note:** You'll need a running MQTT serve running in your network. 
E.g. mosquitto.


## Step 4
Publish the reading from your sensor via MQTT to the server. 
We are also moving the connection to the wifi into the `boot.py`.


**Note**

Even though I ran this successfully on a NodeMCU ESP8266 you might 
have to tweak the one or other part of the code. ;-) 
