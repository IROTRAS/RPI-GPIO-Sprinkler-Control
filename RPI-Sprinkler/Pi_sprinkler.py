import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import os
import RPi.GPIO as GPIO
import argparse
import signal
import sys
import time
import socket
import logging
import json
import subprocess

# --------------------------------------------------------------
### Initial Setup
# --------------------------------------------------------------

### GPIO setup
# ingore any warnings
GPIO.setwarnings(False)
# Declare variables
GPIO.setmode(GPIO.BCM)
# Sprinkler Zones
Z1 = 21     #Orange
Z2 = 2      #Pink
Z3 = 3      #Yellow
Z4 = 4      #Purple
Z5 = 5      #Green
Z6 = 6      #Grey
Z7 = 7      #Brown
Z8 = 8      #
Z9 = 9      #
Z10 = 10    #
Z11 = 11    #
Z12 = 12    #

# setup GPIO pins to all be output
GPIO.setup(Z1,GPIO.OUT)
GPIO.setup(Z2,GPIO.OUT)
GPIO.setup(Z3,GPIO.OUT)
GPIO.setup(Z4,GPIO.OUT)
GPIO.setup(Z5,GPIO.OUT)
GPIO.setup(Z6,GPIO.OUT)
GPIO.setup(Z7,GPIO.OUT)
GPIO.setup(Z8,GPIO.OUT)
GPIO.setup(Z9,GPIO.OUT)
GPIO.setup(Z10,GPIO.OUT)
GPIO.setup(Z11,GPIO.OUT)
GPIO.setup(Z12,GPIO.OUT)

#set initial values for GPIO pins to be high (counterintuitive but it's off)
GPIO.output(Z1, GPIO.HIGH)
GPIO.output(Z2, GPIO.HIGH)
GPIO.output(Z3, GPIO.HIGH)
GPIO.output(Z4, GPIO.HIGH)
GPIO.output(Z5, GPIO.HIGH)
GPIO.output(Z6, GPIO.HIGH)
GPIO.output(Z7, GPIO.HIGH)
GPIO.output(Z8, GPIO.HIGH)
GPIO.output(Z9, GPIO.HIGH)
GPIO.output(Z10, GPIO.HIGH)
GPIO.output(Z11, GPIO.HIGH)
GPIO.output(Z12, GPIO.HIGH)


# --------------------------------------------------------------
### Functions
# --------------------------------------------------------------

### MQTT settings
broker = 'Hassio IP'
command_topic = "sprinkler/command"
state_topic = "sprinkler/state"
mqttQos = 0
mqttRetained = False


def post_sprinkler_zone_state(data):
    print('Posting Sprinkler Zone status')
    client.publish(state_topic, data, mqttQos, mqttRetained)  #

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(command_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = str(msg.payload.decode('ascii'))  # decode the binary string
    print(msg.topic + " " + payload)
    process_trigger(payload)

def process_trigger(payload):
    if payload == 'Z1OPEN':
        print('Zone 1 OPEN triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
        

    if payload == 'Z1CLOSE':
        print('Zone 1 CLOSE triggered') 
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)

    if payload == 'Z2OPEN':
        print('Zone 2 OPEN triggered') 
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z2CLOSE':
        print('Zone 2 CLOSE triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)

    if payload == 'Z3OPEN':
        print('Zone 3 OPEN triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z3CLOSE':
        print('Zone 3 CLOSE triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)

    if payload == 'Z4OPEN':
        print('Zone 4 OPEN triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z4CLOSE':
        print('Zone 4 CLOSE triggered') 
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)

    if payload == 'Z5OPEN':
        print('Zone 5 OPEN triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z5CLOSE':
        print('Zone 5 CLOSE triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z6OPEN':
        print('Zone 6 OPEN triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z6CLOSE':
        print('Zone 6 CLOSE triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z7OPEN':
        print('Zone 7 OPEN triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z7CLOSE':
        print('Zone 7 CLOSE triggered') 
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z8OPEN':
        print('Zone 8 OPEN triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z8CLOSE':
        print('Zone 8 CLOSE triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z9OPEN':
        print('Zone 9 OPEN triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z9CLOSE':
        print('Zone 9 CLOSE triggered') 
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z10OPEN':
        print('Zone 10 OPEN triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z10CLOSE':
        print('Zone 10 CLOSE triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z11OPEN':
        print('Zone 11 OPEN triggered') 
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z11CLOSE':
        print('Zone 11 CLOSE triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z12OPEN':
        print('Zone 12 OPEN triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)
    
    if payload == 'Z12CLOSE':
        print('Zone 12 CLOSE triggered')
        post_sprinkler_zone_state(payload)
        sprinkler_zone_command(payload)

def sprinkler_zone_command(payload): 
    if payload == 'Z1OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z1, GPIO.LOW)
    if payload == 'Z1CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z1, GPIO.HIGH)
    if payload == 'Z2OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z2, GPIO.LOW)
    if payload == 'Z2CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z2, GPIO.HIGH)
    if payload == 'Z3OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z3, GPIO.LOW)
    if payload == 'Z3CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z3, GPIO.HIGH)
    if payload == 'Z4OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z4, GPIO.LOW)
    if payload == 'Z4CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z4, GPIO.HIGH)
    if payload == 'Z5OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z5, GPIO.LOW)
    if payload == 'Z5CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z5, GPIO.HIGH)
    if payload == 'Z6OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z6, GPIO.LOW)
    if payload == 'Z6CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z6, GPIO.HIGH)
    if payload == 'Z7OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z7, GPIO.LOW)
    if payload == 'Z7CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z7, GPIO.HIGH)
    if payload == 'Z8OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z8, GPIO.LOW)
    if payload == 'Z8CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z8, GPIO.HIGH)
    if payload == 'Z9OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z9, GPIO.LOW)
    if payload == 'Z9CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z9, GPIO.HIGH)
    if payload == 'Z10OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z10, GPIO.LOW)
    if payload == 'Z10CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z10, GPIO.HIGH)
    if payload == 'Z11OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z11, GPIO.LOW)
    if payload == 'Z11CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z11, GPIO.HIGH)
    if payload == 'Z12OPEN':
        # Turn GPIO Pin high
        GPIO.output(Z12, GPIO.LOW)
    if payload == 'Z12CLOSE':
        # Turn GPIO Pin low
        GPIO.output(Z12, GPIO.HIGH)


print("starting to connect")
client = mqtt.Client()
client.username_pw_set(username='name',password='password')  # need this

client.on_connect = on_connect    # call these on connect and on message
client.on_message = on_message

client.connect(broker)
print("connected")
client.loop_start()    #  run in background and free up main thread



# ### RF
# # pyli disabe=unused-argument
# def exitandler(signal, frame):
#     rfvice.cleanup()
#     sys.exit(0)

# logging.basiConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
#                     format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

try:
    while True:
        pass
finally:
    client.loop_stop()
    GPIO.cleanup()