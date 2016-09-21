# /arduino

This directory contains projects requiring an Arduino to be connected to the Raspberry Pi. Plug the Arduino into the Raspberry Pi by the USB cable. That should be all you need to do - the Arduino should light up and start running the program that it has. 

To run the *.ino* files, open then in the Arduino IDE. If that doesn't appear in the top left menu, you need to install it: *sudo apt-get install arduino*

The joystick needs to be plugged into the Arduino in the correct way for it to work. This is:
 * GND (black wire) to Arduino GND
 * +5V (white wire) to Arduino 5v
 * VRx (gray wire) to Arduino analogue pin 0
 * VRy (purple wire) to Arduino anlogue pin 1
 * SW (blue wire) to Arduino digital pin 2

To check if the Arduino end is working, open the Arduino IDE and choose *Tools > Serial Monitor*. You should see x, y, and switch values as they come in. But you shouldn't need to spend any time in the Arduino IDE.

*arduinojoystick.py* requires the joystick plugged into the Arduino running *joystick.ino*. It also requires the 4-segment LED matrix to be plugged in and the buzzer (wiring as in *lights.py*). When run, it should disply the movements of the joystick on the LED matrix.
