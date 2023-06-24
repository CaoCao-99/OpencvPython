#Twist picture
import cv2
import numpy as np

img = cv2.imread("Resources/lamborgini.jpg")
width, height = 200,300

pts1 = np.float32([[111,219],[141,219],[111,300],[141,300] ])
pts2 = np.float32([[0,0],[width, 0],[0,height],[width   ,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Warp Image", imgOutput)
cv2.waitKey(0)
