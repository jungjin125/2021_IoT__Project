from lcd  import drivers  #lcd에 drivers 있다
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 9

display = drivers.Lcd()

try:

    while True:  
        now= datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"),1)
        time.sleep(0.5)
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            display.lcd_display_string('T=%.1f*C,H=%.1f%%' % (t, h),2)
        else:
            print('Read Error')

finally:
    print("Cleaning up!")
    display.lcd_clear()
