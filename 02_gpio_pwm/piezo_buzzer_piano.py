# 도레미파솔라시도 음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#pwm 인스턴스 생성
#주파수 설정(4옥타브 도음 : 262Hz)
pwm=GPIO.PWM(BUZZER_PIN,262)
pwm.start(10) #duty cycle (0~100)

#도레미파솔라시도 소리내기
melody = [262, 294, 330, 349, 392, 440, 494, 523]  #리스트
first = [392, 392, 440, 440, 392, 392, 330, 330, 392, 392, 330, 330, 294, 294, 392, 392, 440, 440, 392, 392, 330, 330, 392, 330, 294, 330, 262]

try:
    for i in first:
        pwm.ChangeFrequency(i)  #주파수 변경
        time.sleep(0.3)

finally:
    pwm.stop()
    GPIO.cleanup()