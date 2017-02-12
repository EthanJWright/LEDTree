import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#BUTTON SETUP
button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#LED SETUP
led = 21
GPIO.setup(led, GPIO.OUT)
#Switch on

while True:
  input_state = GPIO.input(button)
  if input_state == False:
    print('Button Pressed')

    GPIO.output(led, 1)
    time.sleep(2)
    GPIO.output(led, 0)
    # Switch on LED 
