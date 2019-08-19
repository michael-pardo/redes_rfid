#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setmode(GPIO.BCM)

reader = SimpleMFRC522()
GPIO.setup(18,GPIO.OUT)

try:
        while True:
            id, text = reader.read()
            GPIO.output(18,True)
            time.sleep(3)
            GPIO.output(18,False)
            
            
            print("Soy "+text)
finally:
        GPIO.cleanup()
