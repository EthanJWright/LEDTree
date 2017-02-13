import requests
import json
#Documentation for API: https://darksky.net/dev/docs/response
class Weather(object):
    def __init__(self):
        self.temp = 0
        self.cloud_cover = 0
        self.wind_speed = 0

    def set_temp(self, _temp):
        self.temp = _temp

    def set_cloud_cover(self, _cloud_cover):
        self.cloud_cover = _cloud_cover

    def set_wind_speed(self, _wind_speed):
        self.wind_speed = _wind_speed

    def get_wind_speed(self):  #The wind speed in miles per hour.
        return self.wind_speed

    def get_cloud_cover(self):  #The percentage of sky occluded by clouds, between 0 and 1, inclusive.
        return self.cloud_cover


    def get_temp(self):         #The air temperature in degrees Fahrenheit.
        return self.temp
  
    def refresh(self):
        url = 'https://api.forecast.io/forecast/52347449fab1dab5431fcbc264efcb19/40.014984,-105.270546'
        f = requests.get(url).json()
        current = f['currently']

        self.set_temp(current['temperature'])
        self.set_cloud_cover(current['cloudCover'])
        self.set_wind_speed(current['windSpeed'])






myVar = Weather()
myVar.refresh()

print myVar.temp






