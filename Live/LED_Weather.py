from LED_Template import LED
import time
class LED_Weather(LED):
    def update(self):
        #Sets up the panel variables
        print 'CALLING API --------------------------'
        self.user.tempAPI.refresh()
        self.new_panel[0] = self.user.tempAPI.temp + self.user.weather_offset
        self.new_panel[1] = self.user.tempAPI.cloud_cover
        self.new_panel[2] = self.user.tempAPI.time
        #With new values set, start fading to the new values
        self.fade_LED()

#Must call begin first time this is run
    def begin(self):
        print 'CALLING API ------------------------'
        #This is required to set up difference between new and old
        self.user.tempAPI.refresh()
        self.new_panel[0] = self.user.tempAPI.temp + self.user.weather_offset
        self.new_panel[1] = self.user.tempAPI.cloud_cover
        self.new_panel[2] = self.user.tempAPI.time
        for i in range(0, 3):
            self.old_panel[i] = self.new_panel[i]
            self.set_RGB(self.get_RGB(i), i)
        time.sleep(self.user.api_call_interval)



    def set_temp(self):
        #Temp will get the 
        #Fit variables are coefficients for the regression model
        #Regression calculations found in MATLAB file
        fit = [None] * 3
        rgb = [None] * 3
        #regression coefficients
        fit[0] = [0.1504, -16.8053, 509.9143]
        fit[1] = [-0.1473, 19.2913, -410.0381]
        fit[2] = [-0.0042, -3.7102, 368.9524]
        temp = self.old_panel[0]

        for color in range(0, 3):
            rgb[color] = self.get_regression(fit[color], temp)

        rgb = self.check_RGB(rgb)
        print rgb, 'TEMP RGB at temp', temp
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
        start_early = 15

        sun_up = self.user.tempAPI.sun_up - start_early
        sun_down = self.user.tempAPI.sun_down - start_early

        diff_up = time - sun_up
        diff_down = time - sun_down

        end_of_day = 1440
        sunrise_interval = 30
        #If 15 minutes before sunrise
        if( 0 <= (diff_up) < sunrise_interval ):
            #sun is rising
            rgb = self.set_sun(diff_up)
            print 'time rgb', rgb
            return rgb
        #If 15 minutes before sunset
        elif(0 <= (diff_down) < sunrise_interval):
            #sun is setting
            rgb = self.set_sun(sunrise_interval - diff_down)
            print 'time rgb', rgb
            return rgb
        #If night
        elif((0 < time < sun_up) or (sun_down + sunrise_interval < time < end_of_day)):
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
        rgb = [None] * 3
        if(panel_number == 0):
            rgb = self.set_temp()
        elif(panel_number == 1):
            rgb = self.set_cloud()
        elif(panel_number == 2):
            rgb = self.set_time()
        return rgb
