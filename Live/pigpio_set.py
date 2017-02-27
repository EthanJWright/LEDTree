#!/usr/bin/env python
import pigpio

class pig_rgb():
    def __init__(self):
        self.rpi = pigpio.pi()
        self.gpio_1 = [None] * 3

    def pig_set(self, panel, rgb):
        if(panel == 0):
            for i in range (0, 3):
                self.rpi.set_PWM_dutycycle(self.gpio_1[i], rgb[i])

    def pig_begin(self, gpio):
        self.gpio_1[0] = gpio[0]
        self.gpio_1[1] = gpio[1]
        self.gpio_1[2] = gpio[2]

    def pig_end(self):
        self.rpi.stop()


