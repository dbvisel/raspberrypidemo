import RPi.GPIO as GPIO  ## import gpio library
import time ## import time so that we can pause

# setup stuff!

led1 = 24
led2 = 23
led3 = 22
led4 = 27
led5 = 18
buzzerpin = 17

GPIO.setmode(GPIO.BCM)           ## use board pin numbering
GPIO.setup(led1, GPIO.OUT)       ## set up led 1 pin, white wire
GPIO.setup(led2, GPIO.OUT)       ## set up led 2 pin, orange wire
GPIO.setup(led3, GPIO.OUT)       ## set up led 3 pin, green wire
GPIO.setup(led4, GPIO.OUT)       ## set up led 4 pin, yellow wire
GPIO.setup(led5, GPIO.OUT)       ## set up led 5 pin, purple wire
GPIO.setup(buzzerpin, GPIO.OUT)  ## set up buzzer pin, blue wire


def Blink(pin, iterations, speed):

# pin: the pin you want to blink
# iterations: the number of times this should happen
# speed: how long each blink should be (in seconds)

   print("Looping pin " + str(pin))
   for i in range(0,iterations):
       print("Iteration " + str(i+1))
       GPIO.output(pin, True)
       time.sleep(speed)
       GPIO.output(pin, False)
       time.sleep(speed)
   print("Done")


def TurnOn(pin, timeon):

# pin: the pin you want to turn on
# timeon: how long you want the pin on (in seconds)

   GPIO.output(pin, True)
   time.sleep(timeon)
   GPIO.output(pin, False)


def AllOn(timeon):

# timeon: how long you want the lights on (in seconds)

   GPIO.output(led1, True)
   GPIO.output(led2, True)
   GPIO.output(led3, True)
   GPIO.output(led4, True)
   GPIO.output(led5, True)
   time.sleep(timeon)
   GPIO.output(led1, False)
   GPIO.output(led2, False)
   GPIO.output(led3, False)
   GPIO.output(led4, False)
   GPIO.output(led5, False)


# end of all the definitions!

Blink(buzzerpin, 3, 0.1)

Blink(led1, 4, 0.125)
Blink(led2, 4, 0.125)
Blink(led3, 4, 0.125)
Blink(led4, 4, 0.125)
Blink(led5, 4, 0.125)

AllOn(1)

TurnOn(buzzerpin, 1)

GPIO.cleanup() ## when we're done, turn everything off.
