import LED_Weather
import time

LED = LED_Weather.LED_Weather()
LED.begin()

while(True):
    print 'TIME: ', time.ctime()
    LED.update()
    print 'Updating'
