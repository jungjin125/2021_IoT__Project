import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera Open failed')
    exit()

# xnl 필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')





while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
    if not ret:
        break
    cv2.imshow('frame',frame)
   # out.write(frame)
    #1000 -> 1초  10-.0.01초
    if cv2.waitKey(10)==13:
        break


cv2.imshow('image',frame)
cv2.waitKey(0)
cv2.destroyAllwindows()
