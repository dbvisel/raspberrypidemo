# Simple relay demo
#
# Make sure:
#
# 1) pin IO19 goes to the relay (blue wire)
# 2) the two wires going out of the relay (red and brown) are connectd
#    to the blue connector on the cord of the laser light show; it does
#    not matter which goes to which
# 3) that laser light show is on
#
# How this works: when the relay pin is true, the switch from the relay is
# closed. When that switch is closed, the laser light show can play. When
# it's not, it won't go.


import RPi.GPIO as GPIO
import time

relaypin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(relaypin, GPIO.OUT)

GPIO.output(relaypin, True)
time.sleep(1)
GPIO.output(relaypin, False)

GPIO.cleanup()
