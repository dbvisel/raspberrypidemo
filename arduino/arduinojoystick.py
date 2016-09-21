# this requires an Arduino plugged into the USB running joystick.ino
# port should be ttyACM0 by default, but sometimes it can switch to ttyACM1


import RPi.GPIO as GPIO  ## import gpio library
import max7219.led as led
import time
import serial

buzzerpin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerpin, GPIO.OUT)

ser = serial.Serial('/dev/ttyACM0', 115200);
matrix = led.matrix(cascaded=4, vertical=True)

xmiddle = 510 # this is what it comes out with with no movement
ymiddle = 525 # this what it comes out with with no movement

while 1 :
    rcv = ser.readline()
    comtype = rcv[0:6]
    if(rcv[8:-1].isdigit()):
        comval = int(rcv[8:-1])
    else:
        comval = 9999
    if(comtype == "Switch"):
        if(comval == 0):
            matrix.letter(0, ord("*"))
            GPIO.output(buzzerpin, True)
        else:
            matrix.letter(0, ord(" "))
            GPIO.output(buzzerpin, False)
    if(comtype == "x-axis"):
        print("x-axis!")
        if(comval > xmiddle):
            print("left! " + repr(comval))
            matrix.letter(1, ord("<"))
        else:
            matrix.letter(1, ord(" "))
        if(comval < xmiddle):
            print("right! " + repr(comval))
            matrix.letter(3, ord(">"))
        else:
            matrix.letter(3, ord(" "))
    if(comtype == "y-axis"):
        print("y-axis!")
        if(comval > ymiddle):
            print("down! "+repr(comval))
            matrix.letter(2, ord("v"))
        else:
            matrix.letter(2, ord(" "))
        if(comval < ymiddle):
            print("up! " + repr(comval))
            matrix.letter(2, ord("^"))
        else:
            matrix.letter(2, ord(" "))
                          
