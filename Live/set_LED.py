import requests
import time
import json
import datetime
import get_weather
# MAKE: #TODO calculate_RGB w/ a sub function calculate(tempAPI.temp, tempAPI.cloud_cover, tempAPI.time)
#TODO RGP.temp.red RGB.temp.blue


#to make first call, call LED.begin(), then every time to make new call call LED.update()
class LED(object):
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


    def fade_LED(self):
        for i in range(0, int(self.get_max())):
            for j in range(0, 2):
                if(int(self.new_panel[j]) < int(self.old_panel[j])):
                    self.old_panel[j] -= 1
                    print self.old_panel[j]
                elif(int(self.new_panel[j]) > int(self.old_panel[j])):
                    self.old_panel[j] += 1
                    print self.old_panel[j]
            time.sleep(.001)
            print 'did something' 
            #TODO set_RGB using self.old in ever print statement above
        for i in range(0, 2):
            self.old_panel[i] = self.new_panel[i]

#Start of unique to inheritance
    def update(self):
        tempAPI = get_weather.Weather()
        tempAPI.refresh()
        self.new_panel[0] = tempAPI.temp*100
        self.new_panel[1] = (tempAPI.cloud_cover * 10)
        self.new_panel[2] = tempAPI.time
        print self.old_panel[0]

        self.fade_LED()

#Must call begin first time this is run
    def begin(self):
        tempAPI = get_weather.Weather()
        tempAPI.refresh()
        self.new_panel[0] = tempAPI.temp*100
        self.new_panel[1] = (tempAPI.cloud_cover * 10)
        self.new_panel[2] = tempAPI.time
        for i in range(0, 2):
            self.old_panel[i] = self.new_panel[i]




'''
    def set_LED(self): 
        #TODO Calculate RGB values for input
        temp_rgb = calculate_temp(self.new_panel[0])
        cloud_rgb = calculate_cloud(self.new_panel[1])
        time_rgb = calculate_time(self.new_panel[2])
'''

