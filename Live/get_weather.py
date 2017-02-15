import requests
import json
import datetime
#Documentation for API: https://darksky.net/dev/docs/response
class Weather(object):
    def __init__(self):
        self.temp = 0        #The air temperature in degrees Fahrenheit.
        self.cloud_cover = 0  #The percentage of sky occluded by clouds, between 0 and 1, inclusive.
        self.wind_speed = 0     #The wind speed in miles per hour.
        self.time = 0
        self.url = 'https://api.darksky.net/forecast/52347449fab1dab5431fcbc264efcb19/40.014984,-105.270546'
  
    def refresh(self):
        data = requests.get(self.url).json()
        current = data['currently']
        self.temp = current['temperature']
        self.cloud_cover = current['cloudCover']
        self.wind_speed = current['windSpeed']
        self.time = current['time']





'''
myVar = Weather()
myVar.refresh()



print myVar.temp
print myVar.cloud_cover * 100, 'percentage of cloud coverage'
print myVar.wind_speed, ' MPH winds'


hours = int(datetime.datetime.fromtimestamp(int(myVar.time)).strftime('%H')) - 7
minutes = int(datetime.datetime.fromtimestamp(int(myVar.time)).strftime('%M'))
print hours,':',minutes
'''
