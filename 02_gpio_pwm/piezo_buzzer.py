# 도 음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#pwm 인스턴스 생성
#주파수 설정(4옥타브 도음 : 262Hz)
pwm=GPIO.PWM(BUZZER_PIN,262)
pwm.start(10) #duty cycle (0~100)

time.sleep(2)
pwm.ChangeDutyCycle(0)  #부저음이 나지 않음

pwm.stop()
GPIO.cleanup()