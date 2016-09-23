# Relay demo with joystick
#
# Make sure:
#
# 1) pin IO19 goes to the relay (blue wire)
# 2) the two wires going out of the relay (red and brown) are connectd
#    to the blue connector on the cord of the laser light show; it does
#    not matter which goes to which
# 3) that laser light show is on
# 4) that the Arduino with joystick is plugged into a USB port. It should
#    be running the same joystick program
#
# What this does: every time you hit the joystick button, the laser light show
# toggles - if it's off, it turns on, if it's on, it turns off. This is a
# slightly more complicated version of relayjoystick.py - it's showing that the
# relationship between input and output can be arbitrary

import RPi.GPIO as GPIO
import time
import serial

# setup stuff

relaypin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(relaypin, GPIO.OUT)

relayflag = False

ser = serial.Serial('/dev/ttyACM0', 115200);

# this loops infinitely:

while True:
   rcv = ser.readline()
   comtype = rcv[0:6]
   if(rcv[8:-1].isdigit()):
       comval = int(rcv[8:-1])
   else:
       comval = 9999
   if(comtype == "Switch"):
       if(comval == 0):   # Here is what we do if the button is pressed
           print("Button pressed!")
           relayflag = not relayflag # if relayflag is true, make it false;
                                     # if relayflag is false, make it true
           GPIO.output(relaypin, relayflag)
           time.sleep(0.25) # this makes it less sticky

GPIO.cleanup()
