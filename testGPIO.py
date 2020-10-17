#i/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
while True:
    data = raw_input("Insert GPIO number to check status (blank to quit): ")
    if data == '':
        break
    try:
        number = int(data)
    except:
        continue
    GPIO.setup(number, GPIO.IN)
    st = GPIO.input(number)
    print st
