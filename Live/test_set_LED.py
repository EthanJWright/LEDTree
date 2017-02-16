import set_LED
import time

LED = set_LED.LED()
LED.begin()

while(True):
    LED.update()
    time.sleep(600)


