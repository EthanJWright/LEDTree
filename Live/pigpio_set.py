import pigpio
import sys
import time
rpi = pigpio.pi()
if not rpi.connected:
  sys.exit(1)

rpi.set_PWM_dutycycle(24, 0)
rpi.set_PWM_dutycycle(17, 0)


rpi.set_PWM_dutycycle(22, 255)
time.sleep(2)
rpi.set_PWM_dutycycle(24, 255)
time.sleep(2)
rpi.set_PWM_dutycycle(17, 255)
time.sleep(5)

rpi.set_PWM_dutycycle(17, 0)
rpi.set_PWM_dutycycle(22, 0)
rpi.set_PWM_dutycycle(24, 0)





rpi.stop()


