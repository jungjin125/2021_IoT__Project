#7segment.py
import RPi.GPIO as GPIO
import time

# GPIO 7개 핀 설정(A~G)
#               A  B  C  D  E  F  G
SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

    #Common Cathode : ON-> HIGH,  OFF -> LOW
    data = [1, 1, 1, 1, 1, 1, 0]

    try:
        

                
    finally:
    GPIO.cleanup()
    print('bye')