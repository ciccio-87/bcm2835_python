#!/usr/bin/python

from bcm2835 import *
import sys

PIN = 18 #BCM pin number
ledOn = False

if not bcm2835_init():
	print "Cannot initialize library, retry as root?"
	sys.exit(1)

bcm2835_gpio_fsel(PIN, BCM2835_GPIO_FSEL_OUTP)

while True:
	try:
		ledOn = not ledOn
		bcm2835_gpio_write(PIN, ledOn)
		bcm2835_delay(500)
	except:
		bcm2835_gpio_write(PIN, LOW)
		bcm2835_close()
		break
