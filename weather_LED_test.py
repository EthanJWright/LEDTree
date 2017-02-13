import RPi.GPIO as GPIO
import time
import Weather

GPIO.setmode(GPIO.BCM)
#LED SETUP

led = 21
GPIO.setup(led, GPIO.OUT)
#Switch on

tempAPI = Weather()
tempAPI.refresh()

def LED_weather(temp):
    if ( tempAPI.temp < 50 ):
        GPIO.output(led, 1)
    else:
        GPIO.output(led, 0)

while True:
    tempAPI.refresh()
    LED_weather(temp)
    sleep(60)
