# Warp Prespective

import cv2
import numpy as np

width, height = 250, 350

img = cv2.imread("Resources/kings.jpg")

pts1 = np.float32([ [411, 70], [600, 70], [411, 354], [600, 354] ])
pts2 = np.float32([ [0, 0], [width, 0], [0, height], [width, height] ])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOut)

cv2.waitKey(0)