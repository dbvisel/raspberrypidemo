## This will only work in Python 2!
##
## It's from https://github.com/rm-hull/max7219
## 
## If it doesn't work, you're going to need to follow directions there 
## (on installing SPI) to get this to work!

## Wire connections:
## VCC (red wire) goes to +5V
## GND (black wire) goes to ground
## DIN (white wire) goes to pin 10
## CS (gray wire) goes to pin 8
## CLK (purple wire) goes to pin 11

import max7219.led as led

device = led.matrix()
device.show_message("Hello world!")
