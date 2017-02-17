import time
import datetime
#to make first call, call LED.begin(), then every time to make new call call LED.update()
#Class must be inherited, let fade_LED function according to model you are representing
class LED:
    def __init__(self):
        self.new_panel = [None] * 3
        self.old_panel = [None] * 3

    def get_max(self):
        diff = [None] * 3
        for i in range(0, 2):
            diff[i] = abs(self.new_panel[i] - self.old_panel[i])
        if(diff[0] > diff[1]):
            if(diff[0] > diff[2]):
                return diff[0]
            else:
                return diff[2]
        else:
            return diff[1]

    def set_RGB(self, panel_number):
        print 'This needs to be overwritten', panel_number
        raise NotImplementedError

    def fade_LED(self):
        test = self.set_RGB(0)
        test = self.set_RGB(1)
        test = self.set_RGB(2)
        for i in range(0, int(self.get_max())):
            print 'MAX IS: ', self.get_max()
            for j in range(0, 2):
                if(int(self.new_panel[j]) < int(self.old_panel[j])):
                    self.old_panel[j] -= 1
                    print self.old_panel[j]
                    test = self.set_RGB(j)
                elif(int(self.new_panel[j]) > int(self.old_panel[j])):
                    self.old_panel[j] += 1
                    print self.old_panel[j]
                    test = self.set_RGB(j)
            time.sleep(1)
            print 'did something'
            #TODO set_RGB using self.old in ever print statement above
        for i in range(0, 2):
            self.old_panel[i] = self.new_panel[i]


    def get_regression(self, fit, x_value):
        regression = fit[0] * (pow(x_value, 2)) + fit[1] * (x_value) + fit[2]
        return int(regression)
