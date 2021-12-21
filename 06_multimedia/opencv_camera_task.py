import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera Open failed')
    exit()



while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edge1 = cv2.Canny(frame,50,100)
    if not ret:
        break
    cv2.imshow('output.jpg',frame)
    cv2.imshow('gray.jpg',gray)
    cv2.imshow('edge.jpg',edge1)
   # out.write(frame)
    #1000 -> 1초  10-.0.01초
    if cv2.waitKey(10)==13:
        break


cap.release()
#out.release()
cv2.destroyAllwindows()