
#!/usr/bin/env python
import random, time
import RPi.GPIO as GPIO
class gpio_set(Object):
    # Set GPIO to Broadcom system and set RGB Pin numbers
    def __init__(self):
        self.red = 0        #The air temperature in degrees Fahrenheit.
        self.green = 0  #The percentage of sky occluded by clouds, between 0 and 1, inclusive.
        self.blue = 0     #The wind speed in miles per hour.

    def setter(rgb):
        RUNNING = True
        GPIO.setmode(GPIO.BCM)
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]

        # Set pins to output mode
        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        GPIO.setup(blue, GPIO.OUT)
