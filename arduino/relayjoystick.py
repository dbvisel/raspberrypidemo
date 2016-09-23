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
# What this does: when the joystick button is pressed, the laser light show is
# turned on. When it's not pressed it's not turned on.
#
# After this, look at relaytoggle.py which is very similar.


import RPi.GPIO as GPIO
import time
import serial

# setup stuff

relaypin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(relaypin, GPIO.OUT)

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
           GPIO.output(relaypin, True)
       else: # Here is what we do if the button is not pressed
           GPIO.output(relaypin, False)

GPIO.cleanup()
