import cv2
import numpy as np

img = np.zeros((200,512,3),np.uint8)
# print(img)
#
# img[100:500] = 0,0,255  #Change specific space's color

cv2.line(img,(0,0), (300,300), (0,255,0),3) #img, Start_Point(X,Y), End_Point(X,Y), Color(B,G,R), Thickness
cv2.rectangle(img,(0,0), (111, 222), (0,100,100),cv2.FILLED)
cv2.circle(img, (img.shape[1]//2,img.shape[0]//2), 30, (155,155,5),8)
cv2.putText(img, " OPENCV ",(img.shape[1]//2 - 50,img.shape[0]//2 - 20), cv2.FONT_ITALIC, 3, (0,200,0))

cv2.imshow("Image", img)

cv2.waitKey(0)
