import cv2 as cv

img = cv.imread('images\download (3).jpeg')
#cv.imshow('Image', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)


haar_cascade = cv.CascadeClassifier('detect.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255), thickness=3)

cv.imshow('Image', img)

cv.waitKey(0)