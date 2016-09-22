# Setting up a Raspberry Pi to use these files

(Assuming that the Raspberry Pi already has Raspian installed on it.)

From the terminal:

 * *sudo apt-get update*
 * *sudo apt-get install arduino*
 * *sudo apt-get install iceweasel*
 * *git clone https://github.com/dbvisel/raspberrypidemo.git*
 * *sudo raspi-config*
  * Go down to *9, Advanced Options*
  * Choose *A5, SPI*
  * Select *Yes* to enable to SPI interface
 * Restart the computer

There should now be a directory called *raspberrypidemo* which has the files that you'll use in it.
