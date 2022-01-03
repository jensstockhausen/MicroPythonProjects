# Tutorial

Short walkthrough to get an small ESP8266 project up and running.

Use the project folder as your sandbox and work on these files based 
on the examples in the steps folder.

Run the `setup_venv.sh` to setup your virtual env for python for interacting with the ESP via commandline (esptool, etc.)

For development I'd suggest the Thonny IDE.

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
