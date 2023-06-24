import cv2
# Image Show
img = cv2.imread("Resources/lena.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)


#Video Show
cap = cv2.VideoCapture(0)
cap.set(3, 1300)    #width
cap.set(4,480)      #height
cap.set(10, 1000)   #brightness



while True:
    success, img = cap.read()
    cv2.imshow('Videoasdf', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
