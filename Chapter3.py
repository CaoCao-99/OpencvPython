import cv2
import numpy as np

img = cv2.imread("Resources/lamborgini.jpg")

print(img.shape)

imgResize = cv2.resize(img,(300,200))

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)

imgCropped = img[0:200, 200:500]
cv2.imshow("Cropped Img", imgCropped)

cv2.waitKey(0)