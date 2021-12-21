import spidev
import time
import RPi.GPIO as GPIO


#SPI인스턴스 생성
spi = spidev.SpiDev()

# SPI 통신 시작
spi.open(0, 0) #bus:0, dev: 0

# SPI 통신 속도 설정
spi.max_speed_hz = 100000

LED_PIN=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# 채널에서 SPI 데이터 읽기 (0~1023)
def analog_read(channel):
  # [byte_1, byte_2, byte_3]
  # byte_2 : channel config (channel 0) (+8) -> 0000 1000 -> 1000 0000
  ret = spi.xfer2([1, (8 + channel) << 4, 0])
  print(ret)
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out

try:
    while True:
        reading = analog_read(0) #reading(0~1023)
        if (reading<700):  
          GPIO.output(LED_PIN, GPIO.HIGH)
        else:
           GPIO.output(LED_PIN, GPIO.LOW)
        print("Reading=%d" ,reading)
        time.sleep(0.5)
finally:
    spi.close()