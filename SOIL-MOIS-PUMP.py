import os
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)   #SOIL-MOIS MODUI PUMP PIN 17

GPIO.setup(23, GPIO.OUT)  # relay MODUI PUMP PIN 23
GPIO.output(23, GPIO.HIGH) # relay MODUI PUMP STATE-HIGH



while (True):
    
    if GPIO.input(17):
        print("Need to Water The Garden and Water Pump will be Switched On")
      
        GPIO.output(23, GPIO.LOW)
    
        while (True):
            if not GPIO.input(17):
                GPIO.output(23, GPIO.HIGH)
                time.sleep(3)
                break
    else:
           print("Soil has enough Moisture")



        
