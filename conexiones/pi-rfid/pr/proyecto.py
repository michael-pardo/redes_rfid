#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
from uuid import getnode as get_mac
mac=get_mac()
print(mac)
print(hex(mac))

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setwarnings(False)

try:
        while True:
            print("Leyendo...")
            reader = SimpleMFRC522()
            id, text = reader.read()
            
            macString = ' '.join(("%012X" % id)[i:i+2] for i in range(2,10,2))
            print(macString)
            r = requests.post("http://192.168.0.6:8000/registro/", data={'id': macString, 'lector': 'lector02'})
            print(r.status_code, r.reason)
            #print(id)
            print(text)
            GPIO.output(18,True)
            time.sleep(2)
            GPIO.output(18,False)
            
finally:
        GPIO.cleanup()
