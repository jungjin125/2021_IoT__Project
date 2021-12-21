import RPi.GPIO as GPIO

RLED_PIN = 17
YLED_PIN = 27
GLED_PIN = 22


SWITCH_PIN1 = 14
SWITCH_PIN2 = 15
SWITCH_PIN3 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(RLED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(YLED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GLED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        val = GPIO.input(SWITCH_PIN1) #누르지 않으면 0, 누르면 1
        print(val)
        GPIO.output(RLED_PIN,val) #GPIO.HIGH=1  GPIO.LOW=2
        val = GPIO.input(SWITCH_PIN2) #누르지 않으면 0, 누르면 1
        print(val)
        GPIO.output(YLED_PIN,val) #GPIO.HIGH=1  GPIO.LOW=2
        val = GPIO.input(SWITCH_PIN3) #누르지 않으면 0, 누르면 1
        print(val)
        GPIO.output(GLED_PIN,val) #GPIO.HIGH=1  GPIO.LOW=2

finally:
    GPIO.cleanup()
    print('cleanup and exit')