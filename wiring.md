# LEDs and buzzer

Pin numbering on the Raspberry Pi is a complicated mess. The pin references I have are what's written on the shield.

 * Raspberry Pi GND —> black (a black jumper connects both sides of the breadboard)
 * Raspberry Pi pin 17 (IO24) —> white wire —> LED 1
 * Raspberry Pi pin 24 (IO23) —> orange wire —> LED 2
 * Raspberry Pi pin 23 (IO22) —> green wire —> LED 3
 * Raspberry Pi pin 22 (IO27) —> yellow wire —> LED 4
 * Raspberry Pi pin 27 (IO18) —> purple wire —> LED 5
 * Raspberry Pi pin 18 (IO17) —> blue wire —> buzzer

The LED wires are connected to the positive side (long wire, flat side) of the LED; the LED's negative side (short wire) ic connected via a 330 ohm resistor to ground. The buzzer is connected directly to ground.

# LED matrix

Both the 1-segment LED matrix and the 4-segment LED matrix have five pins. To change matrix, disconnect from the device. You'll see the labels on the bottom side of the board.

 * Raspberry Pi (5V) —> Red wire —> Green wire —> VCC (on the matrix)
 * Raspberry Pi (GND) —> Gray wire —> Yellow wire —> GND
 * Raspberry Pi (MOSI) —> White wire —> Orange wire —> DIN
 * Raspberry Pi (CEO) —> Gray wire —> Red wire —> CS
 * Raspberry Pi (SCLK)—> Purple wire —> Brown wire —> CLK

# Arduino and joystick

The joystick needs to be plugged into the Arduino in the correct way for it to work. This is:

 * GND (black wire) to Arduino GND
 * +5V (white wire) to Arduino 5v
 * VRx (gray wire) to Arduino analogue pin 0
 * VRy (purple wire) to Arduino anlogue pin 1
 * SW (blue wire) to Arduino digital pin 2

# Relay

For this to work, the relay needs its two connectors plugged into the cord of the laser light show. 

 * Raspberry Pi (IO19) —> relay
 * Orange + brown wires from the relay to the cord of the laser light show
