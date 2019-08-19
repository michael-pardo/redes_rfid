#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id+"hello blue")
        if (id == 230563673412):
	   print("True")
#          GPIO.output(18,True)
		
        print(text)
finally:
        GPIO.cleanup()
