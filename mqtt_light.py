#!/usr/bin/python3

import paho.mqtt.client as mqtt
import time
import json

from LightPwm import LightPwm
from RFSwitch import RFSwitch
from DimmerSerial import Dimmer_Serial

rf_switch = RFSwitch(17)
led_strip = LightPwm(13)
dimmer_A = Dimmer_Serial( "/dev/ttyUSB0", "A" )
dimmer_B = Dimmer_Serial( "/dev/ttyUSB0", "B" )

broker = "localhost"


def rfswitch_decimal(client, userdata, message):
    val = int(message.payload)
    rf_switch.send_decimal( val )

def rfswitch_timing(client, userdata, message):
    try:
        vals = json.loads(message.payload)
        rf_switch.send_timing( vals )
    except:
        print("Failed to pars JSON : '{}'".format(message.payload))

def light_dimmer_strip(client, userdata, message):
    try:
        val = int(float(message.payload))
        led_strip.set_value( val )
    except:
        print("Failed to parse FLOAT: '{}'".format(message.payload))
        raise

def light_dimmer_A(client, userdata, message):
    #try:
    val = int(float(message.payload))
    dimmer_A.set( val )
    #except:
    #    print("Failed to parse INT: '{}'".format(message.payload))

def light_dimmer_B(client, userdata, message):
    try:
        val = int(float(message.payload))
        dimmer_B.set( val )
    except:
        print("Failed to parse INT: '{}'".format(message.payload))



subs = [
        ("light/dimmer/strip", light_dimmer_strip),
        ("light/dimmer/A", light_dimmer_A),
        ("light/dimmer/B", light_dimmer_B),
        ("rfswitch/decimal", rfswitch_decimal),
        ("rfswitch/timing", rfswitch_timing)
]


def loop():
    client = mqtt.Client("client")
    client.connect(broker)

    #client.on_message=on_message

    for sub in subs:
        client.subscribe(sub[0], 0)
        client.message_callback_add( sub[0], sub[1] )

    client.loop_forever()

def destroy():
    import RPi.GPIO as GPIO
    GPIO.cleanup()



if __name__ == '__main__':
    loop()
    #try:
    #    loop()
    #except:
    #    destroy()

