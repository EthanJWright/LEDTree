import time
#import pigpio_set
import user_variables
#to make first call, call LED.begin(), then every time to make new call call LED.update()
#Class must be inherited, let fade_LED function according to model you are representing
class LED:
    def __init__(self):
    #Change these based on preference
        self.user = user_variables.User_Variables()

        self.gpio = [None] * self.user.number_of_panels
        self.new_panel = [None] * self.user.number_of_panels
        self.old_panel = [None] * self.user.number_of_panels

#       self.rpi = pigpio_set.pig_rgb()
        self.gpio[0] = (17, 22, 24)

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
    #Return the greatest difference between old panels vs. new panels
        diff = [None] * self.user.number_of_panels
        for i in range(0, self.user.number_of_panels):
            diff[i] = abs(self.new_panel[i] - self.old_panel[i])
        return max(diff) 

    def set_RGB(self, rgb, panel_number):
        #TODO implement GPIO setter class
        print rgb, 'SETTING ON PANEL ', panel_number
        if(panel_number == 0):
            print 'Sending gpio: ', self.user.gpio[panel_number], ' with rgb ', rgb
#            self.rpi.pig_begin(self.user.gpio[panel_number], rgb)


    def fade_LED(self):
        maximum = int(self.get_max())
        for update in range(0, maximum):
        #Check all panels for change since last API call
            for panel_number in range(0, self.user.number_of_panels):
            #Update all panels that need it every iteration
                if(int(self.new_panel[panel_number]) < int(self.old_panel[panel_number])):
                #If value has gone down
                    self.old_panel[panel_number] -= 1
                    self.set_RGB(self.get_RGB(panel_number), panel_number)
                elif(int(self.new_panel[panel_number]) > int(self.old_panel[panel_number])):
                #If value has gone up
                    self.old_panel[panel_number] += 1
                    self.set_RGB(self.get_RGB(panel_number), panel_number)
            print 'did something'
            #Once all checked, sleep to properly break up API call ping time
            time.sleep(self.user.api_call_interval / maximum)
        #In case of any float value discrenpancy, set old for next API call
        for panel_number in range(0, self.user.number_of_panels):
            self.old_panel[panel_number] = self.new_panel[panel_number]


    def get_regression(self, fit, x_value):
        #implement quadtratic model
        regression = fit[0] * (pow(x_value, 2)) + fit[1] * (x_value) + fit[2]
        return int(regression)

    def check_RGB(self, rgb):
        for color in range(0,3):
            if(rgb[color] > 255):
                rgb[color] = 255
            if(rgb[color] < 0):
                rgb[color] = 0
        return rgb
