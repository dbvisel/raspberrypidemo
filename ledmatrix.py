## this is python 2 code
##
## from https://github.com/rm-hull/max7219
## you're going to need to follow directions there (on installing SPI)
## to get this to work!


import max7219.led as led

device = led.matrix()
device.show_message("Hellow world!")
