import RPi.GPIO as GPIO
import time
import Weather

GPIO.setmode(GPIO.BCM)
#BUTTON SETUP
button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#LED SETUP
led = 21
GPIO.setup(led, GPIO.OUT)
#Switch on

temp = Weather()
temp.refresh()

button_pressed = False

def button_pressed():
    return not button_pressed

while True:
  input_state = GPIO.input(button)
  if input_state == True:
    button_pressed()
    print('Button Pressed')
  if button_pressed == True:
    GPIO.output(led, 1)
    # Switch on LED 
  else:
    GPIO.output(led, 0)
