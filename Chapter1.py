#
# # Image Show
# img = cv2.imread("Resources/lena.jpg")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)


# Video Show
# cap = cv2.VideoCapture(0)
# cap.set(3, 1300)    #width
# cap.set(4,480)      #height
# cap.set(10, 1000)   #brightness
#
#
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Videoasdf', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpg")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7) , 0)

imgCanny = cv2.Canny(img, 100,100)
imgCanny2 = cv2.Canny(img, 1,200) #threshold1, threshold2

imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)
imgEroded = cv2.erode(imgDialation, kernel, iterations = 1)


cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)

cv2.imshow("Canny Image1", imgCanny)
cv2.imshow("Canny Image2", imgCanny2)

cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("ReDialation Image", imgDialation)

cv2.waitKey(0)

