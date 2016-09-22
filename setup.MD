# Setting up a Raspberry Pi to use these files

(Assuming that the Raspberry Pi already has Raspian installed on it.)

From the terminal:

 * *sudo apt-get update*, which updates its package trees
 * *sudo apt-get install arduino*, which installs Arduino
 * *sudo apt-get install iceweasel*, which installs IceWeasel, necessary if you want to use the Github website
 * *git clone https://github.com/dbvisel/raspberrypidemo.git*, which installs these files
 * *sudo raspi-config*
  * Go down to *9, Advanced Options*
  * Choose *A5, SPI*
  * Select *Yes* to enable to SPI interface
 * Restart the computer

There should now be a directory called *raspberrypidemo* which has the files that you'll use in it.
