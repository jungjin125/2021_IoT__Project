from lcd  import drivers  #lcd에 drivers 있다
import time

display = drivers.Lcd()

try:
    print("writing to display")
    display.lcd_display_string("Hello World!!",1)
    while True:
        #write line of text to first line on display
        display.lcd_display_string("**WELCOME **",2)
        time.sleep(2)
        display.lcd_display_string("  WELCOME   ",2)
        time.sleep(2)
finally:
    print("Cleaning up!")
    display.lcd_clear()
