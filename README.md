# PicoMQTTServoDemo

A Proof of concept demo using MQTT to control Servos using a Raspberry Pi Pico W

## Dependencies

The demo has been built using the following libraries. Copies of whilch are included in the /lib directory.

1. The mqtt_as client from [micropython-mqtt](https://github.com/peterhinch/micropython-mqtt).
2. I created a prototype asyncronous servo library [servo_as](https://github.com/PhilLeach/servo_as) to drive the servos.

## Requirements

This is a list of items used:

1. Raspberry Pi Pico W
2. Waveshare Pico-Servo-Driver
3. 2 SG90 Servos connected to pins 0 & 1
4. A local [Mosquitto](https://mosquitto.org) Broker (or use test.mosquitto.org)

## Getting Started

1. Download/ Clone this repo
2. Add a file secrets.py to the top-level directory with the following content :
```python
SERVER = 'test.mosquitto.org'  # Or the adress of your local MQTT Broker
SSID = '<Your WiFi SSID>'
PW = '<Your WiFi Password'
```
3. Download the project to your pico and run demo.py
4. Send commands using any MQTT Client (e.g.[EasyMQTT](https://www.easymqtt.app)) to topic /PicoMQTTServoDemo/command
```
Servo1 90
Servo2 -45
```
5. Monitor servo status by subscribing to topic /PicoMQTTServoDemo/status
