from set_LED import LED
import get_weather
class LED_Weather(LED):
    def update(self):
        tempAPI = get_weather.Weather()
        tempAPI.refresh()
        self.new_panel[0] = tempAPI.temp*10
        self.new_panel[1] = (tempAPI.cloud_cover)
        self.new_panel[2] = tempAPI.time
        print self.old_panel[0]

        self.fade_LED()

#Must call begin first time this is run
    def begin(self):
        tempAPI = get_weather.Weather()
        tempAPI.refresh()
        self.new_panel[0] = tempAPI.temp*10
        self.new_panel[1] = (tempAPI.cloud_cover)
        self.new_panel[2] = tempAPI.time
        for i in range(0, 3):
            self.old_panel[i] = self.new_panel[i]


    def set_temp(self):
        fit = [None] * 3
        rgb = [None] * 3
        fit[0] = [0.0179, -0.0325, 48.9904]
        fit[1] = [0.0221, -3.9706, 179.0101]
        fit[2] = [0.0130, -3.5969, 236.05575]
        temp = self.old_panel[0]/10
        for i in range(0, 3):
            rgb[i] = self.get_regression(fit[i], temp)

        rgb = self.check_RGB(rgb)
        print rgb, 'TEMP RGB'
        return rgb

    def set_cloud(self):
        rgb = [None] * 3
        fit = [None] * 3
        fit[0] = [-0.0258, 2.8313, 173.9301]
        fit[1] = [-0.0240, 2.4602, 191.9021]
        fit[2] = [-0.0124, 0.7263, 249.6503]
        cloud = self.old_panel[1]

        for i in range(0, 3):
            rgb[i] = self.get_regression(fit[i], cloud)

        print cloud
        rgb = self.check_RGB(rgb)
        print rgb, 'CLOUD RGB'
        return rgb


    def set_time(self):
        #TODO make regression model for time
        print 'TIME'

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
