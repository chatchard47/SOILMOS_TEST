#!/usr/bin/python
# start by import libraries we want tu use
import RPi.GPIO as GPIO
from time import sleep
import os 
 
#GPIO SETUP
pin = 17   #soil moisture sensor pin 17 gpio
pump = 27  #Relay pump pin 27 gpio

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
GPIO.setup(pump, GPIO.OUT)
 

while (True):
    
    if GPIO.input (pin):
            print("Need to Water The Garden and Water Pump will be Switched On")
            GPIO.output(pump, True)
            sleep(10)
            GPIO.output(pump, False)
            sleep(1)
    
    else:
            print("Soil has enough Moisture")
            GPIO.output(pump, True)
            sleep(10)
            
GPIO.cleanup()