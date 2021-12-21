import RPi.GPIO as GPIO

LED_PIN = 17
SWITCH_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#내부풀다운저항

try:
    while True:
        val = GPIO.input(SWITCH_PIN) #누르지 않으면 0, 누르면 1
        print(val)
        GPIO.output(LED_PIN,val) #GPIO.HIGH=1  GPIO.LOW=2

finally:
    GPIO.cleanup()
    print('cleanup and exit')