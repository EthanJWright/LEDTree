import time
import LED_pigpio
import user_variables
#to make first call, call LED.begin(), then every time to make new call call LED.update()
#Class must be inherited, let fade_LED function according to model you are representing
class LED:
    def __init__(self):
    #Change these based on preference
        self.user = user_variables.User_Variables()

       #GPIO is an [n] length array of tuples which correspond to (RGB) values
       #Each value should correspond to the connected GPIO pin on the RPI
        self.gpio = [None] * self.user.number_of_panels

         # New Panel keeps track of the live data pulled from the API
        self.new_panel = [None] * self.user.number_of_panels
        # Old Panel keeps track of data from [n] minutes prior in order to update  evenly
        self.old_panel = [None] * self.user.number_of_panels

        # Create an instance of our rasberry pi
        self.rpi = pigpio_set.pig_rgb()
        # Set the gpio ports for the RPI
        self.rpi.gpio = self.user.gpio[0]

    def get_RGB(self, panel_number):
        #Implement this to get the values for the RGB lights how ever is prefered
        print 'This needs to be overwritten', panel_number
        raise NotImplementedError

    def begin(self):
        #Implementation of this correlates to get_RGB, this should only be called on
        # the first iteration in order to create discrepancy between new panel and old panel
        print 'This needs to be overwritten'
        raise NotImplementedError

    def update(self):
       #Same use as begin except this is called now on every iteration
        print 'This needs to be implemented'
        raise NotImplementedError

    def get_max(self):
    #Return the greatest difference between old panels vs. new panels
        diff = [None] * self.user.number_of_panels
        for i in range(0, self.user.number_of_panels):
            diff[i] = abs(self.new_panel[i] - self.old_panel[i])
        return max(diff)

    def set_RGB(self, rgb, panel_number):
        #Given a panel number and a rgb, set the corresponding GPIO ports
        print rgb, 'SETTING ON PANEL ', panel_number
        if(panel_number == 0):
            rgb = self.check_RGB(rgb)
            rgb = list(map((lambda x:int( x/2.55 )), rgb))
            print "Setting panel", panel_number, 'with rgb value ', rgb
            self.rpi.pig_set(panel_number, rgb)


    def fade_LED(self):
        maximum = int(self.get_max())
        #This will evenly distribute the change in LED values since the last call
        for update in range(0, maximum):
        #Check all panels for change since last API call
            for panel_number in range(0, self.user.number_of_panels):
            #Update all panels that need it every iteration
                if(int(self.new_panel[panel_number]) < int(self.old_panel[panel_number])):
                #If value has gone down
                    self.old_panel[panel_number] -= 1
                    self.set_RGB(self.get_RGB(panel_number), panel_number)
                elif(int(self.new_panel[panel_number]) > int(self.old_panel[panel_number])):
                #If value has gone up
                    self.old_panel[panel_number] += 1
                    self.set_RGB(self.get_RGB(panel_number), panel_number)
            print 'did something'
            #Once all checked, sleep to properly break up API call ping time
            fade_interval = self.user.api_call_interval / maximum
            time.sleep(fade_interval)
        #In case of any float value discrenpancy, set old for next API call
        #TODO see if we can replace with this line
#        self.old_panel = self.new_panel
        for panel_number in range(0, self.user.number_of_panels):
            self.old_panel[panel_number] = self.new_panel[panel_number]


    def get_regression(self, fit, x_value):
        #implement quadratic model
        regression = fit[0] * (pow(x_value, 2)) + fit[1] * (x_value) + fit[2]
        return int(regression)

    def check_RGB(self, rgb):
        #check to make sure RGB values are between 0, 255
        for color in range(0,3):
            if(rgb[color] > 255):
                rgb[color] = 255
            if(rgb[color] < 0):
                rgb[color] = 0
        return rgb
