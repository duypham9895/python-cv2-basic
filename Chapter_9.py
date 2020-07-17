# Face detection

import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")

# Read camera
cap = cv2.VideoCapture(0)

# set width
cap.set(3, 640)

# set height
cap.set(4, 480)

while True:
    success, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(grayFrame, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.putText(frame, "Person", (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# img = cv2.imread("Resources/lena.png")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# cv2.imshow("Image", img)
# cv2.waitKey(0)

# cv2.imshow("Gray", imgGray)
# cv2.waitKey(0)
