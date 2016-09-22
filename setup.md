# Setting up a Raspberry Pi to use these files

(This assumes that the Raspberry Pi you're using already has Raspbian installed on it & running. If not, download the NOOBS image from https://www.raspberrypi.org/downloads/noobs/ and then follow the instructions at http://www.macworld.co.uk/how-to/mac/how-to-set-up-raspberry-pi-3-with-mac-3637490/ to create the SD card. Plug that in, turn on the Pi, and follow the instructions to install Raspbian; this will take a while.)

 * Connect mouse & keyboard
 * Connect to internet

From the Terminal:

 * *sudo apt-get update*, which updates its package trees
 * *sudo apt-get install arduino*, which installs Arduino
 * *sudo apt-get install iceweasel*, which installs IceWeasel, necessary if you want to use the Github website
 * *git clone https://github.com/dbvisel/raspberrypidemo.git*, which installs these files
 * *sudo raspi-config*
  * Go down to *9, Advanced Options*
  * Choose *A5, SPI*
  * Select *Yes* to enable to SPI interface
 * *sudo pip install max7219*, which installs the library for running the LED matrix
 * Restart the computer

There should now be a directory called *raspberrypidemo* which has the files that you'll use in it. Open *.py* files in Python (use 2 rather than 3 if you're using the LED matrix); open *.ino* files in the Arduino IDE.

## Testing

 * Attach the shield connected to the breadboard to the Raspberry Pi
 * In Python, open *lights.py* and run it. The lights should turn on and the buzzer should work.
 * In Python, open *ledmatrix4.py* and run it. The LED matrix should work.

## Setting up the Arduino

If you're going to be using the Arduino IDE:

 * Plug the Arduino's USB into the Raspberry Pi
 * Open the Arduino IDE from the menu (under *Electronics*)
 * Under *Tools*, go to *Board*, and select *Arduino Mega 2560 or Mega ADK* (or another board if that's what you're using)
 * Under *Tools*, go to *Serial Port* and select *dev/ttyACM0* or whatever it says
 * Open *joystick.ino* (it will want to move the sketch, which is fine) and click the *Upload* button
 * Under *Tools*, go to *Serial Monitor*
 * Change the baud rate to *115200 baud*
 * Make sure that it's spitting out recognizable information
 * Close the Arduino IDE
 * In Python, open *arduinojoystick.py* and see if it works.
