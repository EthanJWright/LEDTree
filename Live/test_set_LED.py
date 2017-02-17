import LED_Weather
import time

LED = LED_Weather.LED_Weather()
LED.begin()

while(True):
    LED.update()
    time.sleep(30)


