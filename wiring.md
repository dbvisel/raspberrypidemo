# LED matrix

Both the 1-segment LED matrix and the 4-segment LED matrix have five pins. To change matrix, disconnect from the device. You'll see the labels on the bottom side of the board.

 * Raspberry Pi —> Red wire —> Green wire —> VCC (on the matrix)
 * Raspberry Pi —> Gray wire —> Yellow wire —> GND
 * Raspberry Pi —> White wire —> Orange wire —> DIN
 * Raspberry Pi —> Gray wire —> Red wire —> CS
 * Raspberry Pi —> Purple wire —> Brown wire —> CLK

# Arduino and joystick

The joystick needs to be plugged into the Arduino in the correct way for it to work. This is:

 * GND (black wire) to Arduino GND
 * +5V (white wire) to Arduino 5v
 * VRx (gray wire) to Arduino analogue pin 0
 * VRy (purple wire) to Arduino anlogue pin 1
 * SW (blue wire) to Arduino digital pin 2
