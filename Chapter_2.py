# Basic function

import cv2
import numpy as np

img = cv2.imread("Resources/image-1.jpg")
kernel = np.ones((5,5), np.uint8)

# Convert to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCany = cv2.Canny(img, 300, 400)
imgDialation = cv2.dilate(imgCany, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# cv2.imshow("Gray", imgGray)
# cv2.waitKey(0)
# cv2.imshow("Blur", imgBlur)
# cv2.waitKey(0)
# cv2.imshow("Cany", imgCany)
# cv2.waitKey(0)
cv2.imshow("Dialation", imgDialation)
cv2.waitKey(0)
cv2.imshow("Eroded", imgEroded)
cv2.waitKey(0)
