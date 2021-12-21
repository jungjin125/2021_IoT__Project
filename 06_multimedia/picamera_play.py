import picamera
import time

path = '/home/pi/src4/06_multimedia'

camera = picamera.PiCamera()

try:
    while True:
        now_str = time.strftime("%Y%m%d_%H%M%S")
        cmd = input("photo:1, video:2, exit:9 > ")
        if cmd == "1":
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(3) #카메라 준비시간
            camera.rotation = 180
            camera.capture(path + "/" + now_str + ".jpg")
            print("사진 촬영")
        elif cmd == "2":
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(3) #카메라 준비시간
            camera.rotation = 180
            camera.start_recording(path + "/" + now_str + ".h264")
            print("동영상 촬영")
            input("press enter to stop")
            camera.stop_recording()
        elif cmd == "9":
            break
        else:
            print("incorrect command")

finally:
    camera.stop_preview()