import requests
import json
import datetime
#Powered by Dark Sky: https://darksky.net/forecast
#Documentation for API: https://darksky.net/dev/docs/response
class Weather(object):
    def __init__(self):
        self.temp = 0        #The air temperature in degrees Fahrenheit.
        self.cloud_cover = 0  #The percentage of sky occluded by clouds, between 0 and 1, inclusive.
        self.wind_speed = 0     #The wind speed in miles per hour.
        self.time = 0
        self.api_key = '52347449fab1dab5431fcbc264efcb19'
        self.latitude = '40.014984'
        self.longitude = '-105.270546'
        self.url = 'https://api.darksky.net/forecast/' + self.api_key + '/' + self.latitude + ',' + self.longitude
        self.data = requests.get(self.url).json()

    def is_json(self):
       try:
           self.data = requests.get(self.url).json()
       except ValueError, e:
           return False
       return True

    def refresh(self):
        if(not self.is_json()):
            time.sleep(30)
            refresh()
        current = self.data['currently']
        self.temp = current['temperature']
        self.cloud_cover = current['cloudCover'] * 100
        self.wind_speed = current['windSpeed'] * 10
        self.time = int(datetime.datetime.fromtimestamp(int(current['time'])).strftime('%H'))

myVar = Weather()
myVar.refresh()
print myVar.temp
