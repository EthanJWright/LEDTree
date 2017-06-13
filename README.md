
[Powered by Dark Sky](https://darksky.net/poweredby/)

02/11/2017
Ethan Wright

Install Pigpio: <br />
```
rm pigpio.tar
sudo rm -rf PIGPIO
wget abyz.co.uk/rpi/pigpio/pigpio.tar
tar xf pigpio.tar
cd PIGPIO
make
sudo make install
```

Start Pigpio: <br />
PIGPIO/pigpio

How to set up RBG LED: <br />
http://dordnung.de/raspberrypi-ledstrip/ <br /> 

Edit crontab:
```
crontab -e
@reboot /PIGPIO/pigpio
*/5 * * * * python /rpiLED/Live/LED_Start.py
```



