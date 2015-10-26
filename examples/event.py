#!/usr/bin/python

from bcm2835 import *
import sys

PIN = 22 #BCM pin number

if not bcm2835_init():
	print "Cannot initialize library, retry as root?"
	sys.exit(1)


bcm2835_gpio_fsel(PIN, BCM2835_GPIO_FSEL_INPT)

bcm2835_gpio_set_pud(PIN, BCM2835_GPIO_PUD_DOWN)  # using a pulldown and an high level detection
bcm2835_gpio_hen(PIN)                             # while the original did the opposite

while True:
	try:
		if bcm2835_gpio_eds(PIN):
			bcm2835_gpio_set_eds(PIN)
			print "High level detected on pin %i" % PIN
        	bcm2835_delay(500)
	except:
		print "exception"
    		bcm2835_close()
		break

