# Resizing and Cropping

import cv2

img = cv2.imread("Resources/image-1.jpg")
print(img.shape)

imgResize = cv2.resize(img, (1228, 632))
print(imgResize.shape)

imCropped = img[0:200, 200:800]

cv2.imshow("Image", img)
cv2.imshow("Resize", imgResize)
cv2.imshow("Crop", imCropped)

cv2.waitKey(0)

