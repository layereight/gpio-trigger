#!/usr/bin/python


import sys
import RPi.GPIO as GPIO
import urllib2


#print (sys.argv[1] + " " + sys.argv[2])

gpio=int(sys.argv[1])
url=sys.argv[2]

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#
# bouncetime
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
#
while True:
    GPIO.wait_for_edge(gpio, GPIO.FALLING, bouncetime=200)
    urllib2.urlopen(url)
