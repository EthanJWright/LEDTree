from set_LED import LED
import get_weather
class LED_Weather(LED):
    def update(self):
        tempAPI = get_weather.Weather()
        tempAPI.refresh()
        self.new_panel[0] = tempAPI.temp*100
        self.new_panel[1] = (tempAPI.cloud_cover)
        self.new_panel[2] = tempAPI.time
        print self.old_panel[0]

        self.fade_LED()

#Must call begin first time this is run
    def begin(self):
        tempAPI = get_weather.Weather()
        tempAPI.refresh()
        self.new_panel[0] = tempAPI.temp*100
        self.new_panel[1] = (tempAPI.cloud_cover)
        self.new_panel[2] = tempAPI.time
        for i in range(0, 2):
            self.old_panel[i] = self.new_panel[i]

    def set_temp(self):
        red_fit = [0.0179, -0.0325, 48.9904]
        green_fit = [0.0221, -3.9706, 179.0101]
        blue_fit = [0.0130, -3.5969, 236.05575]
        temp = self.old_panel[0]/100

        r = self.get_regression(red_fit, temp)
        g = self.get_regression(green_fit, temp)
        b = self.get_regression(blue_fit, temp)
        print [r, g, b], 'TEMP RGB'
        return [r,g,b]

    def set_cloud(self):
        red_fit = [-0.0258, 2.8313, 173.9301]
        green_fit = [-0.0240, 2.4602, 191.9021]
        blue_fit = [-0.0124, 0.7263, 249.6503]
        cloud = self.old_panel[1]
        r = self.get_regression(red_fit, cloud)
        g = self.get_regression(green_fit, cloud)
        b = self.get_regression(blue_fit, cloud)
        print [r,g,b], 'CLOUD RGB'
        return [r,g,b]


    def set_time(self):
        #TODO make regression model for time
        print 'TIME'

    def set_RGB(self, panel_number):
        if(panel_number == 0):
            self.set_temp()
        elif(panel_number == 1):
            self.set_cloud()
        elif(panel_number == 2):
            self.set_time()

    '''
    def get_regression(self, fit, x_value):
        regression = fit[0] * (pow(x_value, 2)) + fit[1] * (x_value) + fit[2]
        return regression
'''
