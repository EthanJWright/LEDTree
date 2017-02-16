import RPi.GPIO as GPIO
import time
import get_weather

GPIO.setmode(GPIO.BCM)
#LED SETUP

led = 21
GPIO.setup(led, GPIO.OUT)
#Switch on

tempAPI = get_weather.Weather()
tempAPI.refresh()

def LED_weather(tempAPI):
    if ( tempAPI.temp < 50 ):
        GPIO.output(led, 1)
    else:
        GPIO.output(led, 0)

while True:
    print 'refresh'
    tempAPI.refresh()
    LED_weather(tempAPI)
    time.sleep(600)
