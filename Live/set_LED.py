import time
from pigpio_set import gpio_set
#to make first call, call LED.begin(), then every time to make new call call LED.update()
#Class must be inherited, let fade_LED function according to model you are representing
class LED:
    def __init__(self):
        self.new_panel = [None] * 3
        self.old_panel = [None] * 3
        self.increment_time = 300
        self.current_gpio = pigpio_set.gpio_set()

    def get_RGB(self, panel_number):
        print 'This needs to be overwritten', panel_number
        raise NotImplementedError

    def begin(self):
        print 'This needs to be overwritten'
        raise NotImplementedError

    def update(self):
        print 'This needs to be implemented'
        raise NotImplementedError

    def get_max(self):
        diff = [None] * 3
        for i in range(0, 3):
            diff[i] = abs(self.new_panel[i] - self.old_panel[i])
        if(diff[0] > diff[1]):
            if(diff[0] > diff[2]):
                return diff[0]
            else:
                return diff[2]
        else:
            return diff[1]

    def set_RGB(self, rgb, panel_number):
        #TODO implement GPIO setter class
        print rgb, 'SETTING ON PANEL ', panel_number
        if(panel_number == 1):
            self.current_gpio.setter(rgb)    
            #TODO CALL pigpio

    def fade_LED(self):
        maximum = int(self.get_max())
        for i in range(0, maximum):
            for j in range(0, 3):
                if(int(self.new_panel[j]) < int(self.old_panel[j])):
                    self.old_panel[j] -= 1
                    self.set_RGB(self.get_RGB(j), j)
                elif(int(self.new_panel[j]) > int(self.old_panel[j])):
                    self.old_panel[j] += 1
                    self.set_RGB(self.get_RGB(j), j)
            print 'did something'
            time.sleep(self.increment_time / maximum)
        for i in range(0, 3):
            self.old_panel[i] = self.new_panel[i]


    def get_regression(self, fit, x_value):
        #implement quadtratic model
        regression = fit[0] * (pow(x_value, 2)) + fit[1] * (x_value) + fit[2]
        return int(regression)

    def check_RGB(self, rgb):
        for i in range(0,3):
            if(rgb[i] > 255):
                rgb[i] = 255
            if(rgb[i] < 0):
                rgb[i] = 0
        return rgb
