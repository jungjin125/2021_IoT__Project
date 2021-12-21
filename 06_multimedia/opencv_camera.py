import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera Open failed')
    exit()
    
#카메라 사진 찍기
#ret, frame = cap.read()

#cv2.imshow('frame',frame)
#cv2.imwrite('output.jpg',frame)
#cv2.waitKey(0)
#fourcc(four character code)
#DTVX(avi), MP4V(MP4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DTVX') #('D','I','V','X')
            
                                #frame   framesize
#out = cv2.VideoWriter('output.avi', fourcc,30,(640, 480))

#동영상 촬영
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('output.jpg',frame)
   # out.write(frame)
    #1000 -> 1초  10-.0.01초
    if cv2.waitKey(10)==13:
        break

cap.release()
#out.release()
cv2.destroyAllwindows()