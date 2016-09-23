# Raspberry Pi electronics demos

These are demo files for using with a Raspberry Pi connected to simple electrical components:

 * *lights.py* contains basic code for turning on and off five LEDs and a buzzer.
 * *ledmatrix.py* contains basic code for using an LED matrix. This only works in Python 2.
 * *ledmatrix4.py* contains basic code for using an array of 4 LED matrices. This only works in Python 2.
 * *relay.py* contains basic code to drive a relay, which can control other things.

This code is dependent on the wiring being the same as it is in the setup I've used. The photos can be used as a reference if the wires come loose. The Fritizing diagram (in */layouts*) contains the schematic and board layout.

The files in */arduino* are for running with an Arduino attached to the Raspberry Pi. There are two more programs for controlling the relay in here as well.

*wiring.md* contains instructions for wiring.

*setup.md* contains instructions for setting up your Raspberry Pi so that these files will work.

To install this on your Raspberry Pi, open the Terminal and type *git clone https://github.com/dbvisel/raspberrypidemo.git*. That will install a directory called *raspberrypidemo* with all these files.
