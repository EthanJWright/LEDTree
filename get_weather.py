import requests
import json
#Documentation for API: https://darksky.net/dev/docs/response
class Weather(object):
    def __init__(self):
        self.temp = 0        #The air temperature in degrees Fahrenheit.
        self.cloud_cover = 0  #The percentage of sky occluded by clouds, between 0 and 1, inclusive.
        self.wind_speed = 0     #The wind speed in miles per hour.
  
    def refresh(self):
        url = 'https://api.forecast.io/forecast/52347449fab1dab5431fcbc264efcb19/40.014984,-105.270546'
        f = requests.get(url).json()
        current = f['currently']

        self.temp = current['temperature']
        self.cloud_cover = current['cloudCover']
        self.wind_speed = current['windSpeed']
#        print current


myVar = Weather()
myVar.refresh()

print myVar.temp, ' current temp'
print myVar.cloud_cover * 100, 'percentage of cloud coverage'
print myVar.wind_speed, ' MPH winds'






