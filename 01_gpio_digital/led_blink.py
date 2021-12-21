import RPi.GPIO as GPIO
import time

LED_red = 4
GPIO.setmode(GPIO.BCM)   #GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_red, GPIO.OUT)
GPIO.output(LED_red, GPIO.HIGH)  #1
print("led on")
time.sleep(2)
GPIO.output(LED_red, GPIO.LOW)#0
print("led off")

LED_yello = 17
GPIO.setup(LED_yello, GPIO.OUT)
GPIO.output(LED_yello, GPIO.HIGH)  #1
print("led on")
time.sleep(2)
GPIO.output(LED_yello, GPIO.LOW)#0
print("led off")

LED_green = 26
GPIO.setup(LED_green, GPIO.OUT)
GPIO.output(LED_green, GPIO.HIGH)  #1
print("led on")
time.sleep(2)
GPIO.output(LED_green, GPIO.LOW)#0
print("led off")

GPIO.cleanup()  #GPIO핀상태 초기화w