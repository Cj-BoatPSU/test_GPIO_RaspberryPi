import RPi.GPIO as GPIO

channel = 23
GPIO.setmode(GPIO.BCM)
#GPIO.setwarning(False)
GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel, GPIO.HIGH)

channel_is_on = GPIO.input(channel)

if channel_is_on:
    print "access if"
    print channel_is_on
else:
    print "access else"
    print channel_is_on
GPIO.cleanup()
