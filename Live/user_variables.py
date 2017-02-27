import get_weather
class User_Variables():
    def __init__(self):
        self.number_of_panels = 3
        self.api_call_interval = 300

        self.gpio = [None] * self.number_of_panels
        self.gpio[0] = (17, 22, 24)
        self.gpio[1] = (0, 0, 0)
        self.gpio[2] = (0, 0, 0)

        self.tempAPI = get_weather.Weather() 
        self.tempAPI.api_key = '52347449fab1dab5431fcbc264efcb19'
        self.tempAPI.latitude = '40.014984'
        self.tempAPI.longitude = '-105.270546'
