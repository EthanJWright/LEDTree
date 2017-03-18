import requests
import json
import datetime
import os
import time, threading
#Powered by Dark Sky: https://darksky.net/forecast
#Documentation for API: https://darksky.net/dev/docs/response
class Weather(object):
    def __init__(self):
        self.temp = 0        #The air temperature in degrees Fahrenheit.
        self.cloud_cover = 0  #The percentage of sky occluded by clouds, between 0 and 1, inclusive.
        self.wind_speed = 0     #The wind speed in miles per hour.
        self.time = 0
        self.sun_up = 0
        self.sun_down = 0

        self.api_key = '52347449fab1dab5431fcbc264efcb19'
        self.latitude = '40.014984'
        self.longitude = '-105.270546'

        self.data = requests.Session()

    def test_connection(self):
       try:
           url = 'https://api.darksky.net/forecast/' + self.api_key + '/' + self.latitude + ',' + self.longitude
           self.data = requests.get(url).json()
       except requests.exceptions.RequestException as e:
           print 'exception hit'
           return False
       except requests.exceptions.ValueError as e:
           print 'Invalid JSON handled'
           return False
       return True

    def convert_to_min(self, time):
        minutes = int(datetime.datetime.fromtimestamp(int(time)).strftime('%M'))
        hours = int(datetime.datetime.fromtimestamp(int(time)).strftime('%H'))
        total = minutes + (hours * 60)
        return total


    def refresh(self):
        if(not self.test_connection()):
            time.sleep(30)
            self.refresh()
        current = self.data['currently']
        self.temp = current['temperature']
        self.cloud_cover = current['cloudCover'] * 100
        self.wind_speed = current['windSpeed'] * 10
        self.time = self.convert_to_min(current['time'])
        self.sun_up = self.convert_to_min(int(self.data['daily']['data'][4]['sunriseTime']))
        self.sun_down = self.convert_to_min(int(self.data['daily']['data'][4]['sunsetTime']))

        
test = Weather()
test.refresh()
print test.sun_up
print test.sun_down
print test.time
print 'temp is :',test.temp
