# Read (Image - Video - Webcam)

import cv2

print("Package imported")

# Read image
# img = cv2.imread("Resources/image-1.jpg")
# cv2.imshow("Output 0: ", img)
# cv2.waitKey(0)

# Read video
# cap = cv2.VideoCapture("Resources/cafe.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# Read camera
cap = cv2.VideoCapture(0)

# set width
cap.set(3, 640)

# set height
cap.set(4, 480)

# set brightness
cap.set(10, -100000)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break