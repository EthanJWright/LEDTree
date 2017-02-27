#!/usr/bin/env python
import pigpio

class pig_rgb():
    def __init__(self):
        self.rpi = pigpio.pi()
        self.gpio_1 = [None] * 3

    def pig_set(self, panel, rgb):
        if(panel == 0):
            for i in range (0, 3):
                self.rpi.set_PWM_sutycycle(self.gpio_1[i], rgb[i])

    def pig_end(self):
        self.rpi.stop()


