#! /usr/bin/env python
#
# Fade an LED (or one color of an RGB LED) using GPIO's PWM capabilities.
#
# Usage:
#   sudo python fade.py
#
# @author Jeff Geerling, 2015

import time
import RPi.GPIO as GPIO

# LED pin mapping.
red = 4
green = 17
blue = 18
# Set which LED to use for fading.
#led0 = green

# GPIO Setup.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.output(red, 1)
GPIO.output(green, 1)
GPIO.output(blue, 1)
# Use PWM to fade an LED.
fade1 = GPIO.PWM(red, 100)
fade2 = GPIO.PWM(green, 100)
fade3 = GPIO.PWM(blue, 100)
fade1.start(0)
fade2.start(0)
fade3.start(0)
# Set up variables for the fading effect.
valueR = 0
valueG = 30
valueB = 60
incrementR = 2
incrementG = 2
incrementB = 2

increasingR = True
increasingG = True
increasingB = True
count = 0

while count < 1000:
    fade1.ChangeDutyCycle(valueR)
    if increasingR:
        valueR += incrementR
	time.sleep(0.002)
    else:
        valueR -= incrementR
	time.sleep(0.002)

    if (valueR >= 100):
        increasingR = False

    if (valueR <= 20):
        increasingR = True

    fade2.ChangeDutyCycle(valueG)
    if increasingG:
        valueG += incrementG
        time.sleep(0.002)
    else:
        valueG -= incrementG
        time.sleep(0.002)

    if (valueG >= 100):
        increasingG = False

    if (valueG <= 20):
        increasingG = True

    fade3.ChangeDutyCycle(valueB)
    if increasingB:
        valueB += incrementB
        time.sleep(0.002)
    else:
        valueB -= incrementB
        time.sleep(0.002)

    if (valueB >= 100):
        increasingB = False

    if (valueB <= 20):
        increasingB = True

    time.sleep(0.05)
    count = count + 1

GPIO.cleanup()
