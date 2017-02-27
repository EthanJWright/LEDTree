from set_LED import LED
import time
class LED_Weather(LED):
    def update(self):
        print 'CALLING API --------------------------'
        self.user.tempAPI.refresh()
        #Temp * 10 to allow for more precise increment update
        self.new_panel[0] = (self.user.tempAPI.temp * 10)
        self.new_panel[1] = (self.user.tempAPI.cloud_cover)
        self.new_panel[2] = (self.user.tempAPI.time)

        self.fade_LED()

#Must call begin first time this is run
    def begin(self):
        print 'CALLING API ------------------------'
        #This is required to set up difference between new and old
        self.user.tempAPI.refresh()
        self.new_panel[0] = (self.user.tempAPI.temp * 10)
        self.new_panel[1] = self.user.tempAPI.cloud_cover
        self.new_panel[2] = (self.user.tempAPI.time)
        for i in range(0, 3):
            self.old_panel[i] = self.new_panel[i]
            self.set_RGB(self.get_RGB(i), i)
        time.sleep(self.user.api_call_interval)



    def set_temp(self):
        fit = [None] * 3
        rgb = [None] * 3
        #regression coefficients from MATLAB
        fit[0] = [0.0179, -0.0325, 48.9904]
        fit[1] = [0.0221, -3.9706, 179.0101]
        fit[2] = [0.0130, -3.5969, 236.05575]
        temp = self.old_panel[0]/10
        for color in range(0, 3):
            rgb[color] = self.get_regression(fit[color], temp)

        rgb = self.check_RGB(rgb)
        print rgb, 'TEMP RGB'
        return rgb

    def set_cloud(self):
        rgb = [None] * 3
        fit = [None] * 3
        #regression coefficients from MATLAB
        fit[0] = [-0.0258, 2.8313, 173.9301]
        fit[1] = [-0.0240, 2.4602, 191.9021]
        fit[2] = [-0.0124, 0.7263, 249.6503]
        cloud = self.old_panel[1]

        for color in range(0, 3):
            rgb[color] = self.get_regression(fit[color], cloud)

        rgb = self.check_RGB(rgb)
        print rgb, 'CLOUD RGB'
        return rgb

    def set_sun(self, diff_up):
        rgb = [None] * 3
        fit = [None] * 3
        #regression coefficients from MATLAB
        fit[0] = [-0.6972, 15.0515, 216.7746]
        fit[1] = [-0.3353, 20.9119, -56.9051]
        fit[2] = [1.1388, -31.8291, 246.6106]
        for i in range(0, 3):
            rgb[i] = self.get_regression(fit[i], diff_up)
        return rgb


    def set_time(self):
        rgb = [None] * 3
        time = self.old_panel[2]
        sun_up = self.user.tempAPI.sun_up - 15
        sun_down = self.user.tempAPI.sun_down - 15
        diff_up = time - sun_up
        diff_down = time - sun_down
        #If 15 minutes before sunrise
        if( 0 < (diff_up) < 30 ):
            #sun is rising
            rgb = self.set_sun(diff_up)
            print 'time rgb', rgb
            return
        #If 15 minutes before sunset
        elif(0 < (diff_down) < 30):
            #sun is setting
            rgb = self.set_sun(30 - diff_down)
            print 'time rgb', rgb
            return rgb
        #If night 
        elif((0 < time < sun_up) or (sun_down + 30 < time < 1440)):
            #Make night
            rgb[0] = 255
            rgb[1] = 0
            rgb[2] = 255
            print 'time rgb', rgb
            return rgb
        else:
            #If day
            rgb[0] = 0
            rgb[1] = 255
            rgb[2] = 255
            print 'time rgb', rgb
            return rgb

    def get_RGB(self, panel_number):
        rgb = []
        if(panel_number == 0):
            rgb = self.set_temp()
        elif(panel_number == 1):
            rgb = self.set_cloud()
        elif(panel_number == 2):
            rgb = self.set_time()
        return rgb

    '''
    def get_regression(self, fit, x_value):
        regression = fit[0] * (pow(x_value, 2)) + fit[1] * (x_value) + fit[2]
        return regression
'''
