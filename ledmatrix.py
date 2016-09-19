## this is python 2 code
##
## This code shows a message on an 8 x 8 LED matrix
##
## This is following what's at https://github.com/rm-hull/max7219
## You're going to need to follow directions there (on installing SPI)
## to get this to work on a fresh Raspberry Pi!
##
## For this to work: connect the 1-segment LED matrix to the Raspberry Pi
## Red > Green --> VCC
## Gray > Yellow --> GND
## White > Orange --> DIN
## Gray > Red --> CS
## Purple > Brown --> CLK
##
## This will also work with the 4-segment matrix, but it isn't quite what
## you're expecting. Look at ledmatrix4.py for how to use that.



import max7219.led as led

device = led.matrix()
device.show_message("Hello!")
