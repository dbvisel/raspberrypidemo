## this is python 2 code
##
## This code shows a message on multiple 8 x 8 LED matrices
##
## This is following what's at https://github.com/rm-hull/max7219
## You're going to need to follow directions there (on installing SPI)
## to get this to work on a fresh Raspberry Pi!
##
## For this to work: connect the 4-segment LED matrix to the Raspberry Pi
## Red > Green --> VCC
## Gray > Yellow --> GND
## White > Orange --> DIN
## Gray > Red --> CS
## Purple > Brown --> CLK



import max7219.led as led
import time ## this is only needed for pausing!


device = led.matrix(cascaded=4, vertical=True) # set up device for 4 matrices

device.letter(0, ord('1')) ## this puts the number 1 on the first matrix
device.letter(1, ord('2')) ## on the second matrix
device.letter(2, ord('3')) ## on the third matrix
device.letter(3, ord('4')) ## on the fourth matrix

time.sleep(1) ## a pause!

device.show_message(" ") ## clear the screen

device.show_message("Hello!") ## scroll the message!

## try setting cascaded to 1 - then all cells will be the same
## if you don't have vertical=True, the scrolling will be the other way

time.sleep(1)

device = led.matrix(cascaded=1, vertical=False)

device.show_message("The other way!")


## Other things you could do, not very useful:

time.sleep(1)

device = led.matrix(cascaded=4, vertical=False)

device.show_message("What happens now?")

## Other things you could do, least useful yet:

time.sleep(1)

device = led.matrix(cascaded=1, vertical=True)

device.show_message("Another thing!")
