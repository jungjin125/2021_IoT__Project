import cv2

# xnl 필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

img = cv2.imread('ncttest.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

    #ROI(Region of Interest, 관심영역)

    roi_color = img[y:y+h, x:x+w]
    roi_gray = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)

    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh),(0, 255, 0),2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllwindows()
