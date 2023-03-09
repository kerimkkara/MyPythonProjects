import cv2
import numpy as np

image = cv2.imread('hsv9.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

blur = cv2.medianBlur(hsv, 15)

lower = np.array([24,28,46])
upper = np.array([54,148,232])

mask = cv2.inRange(blur, lower, upper)


kernel = np.ones((3,3),np.uint8)
mask = cv2.erode(mask,kernel,iterations = 3)

res = cv2.bitwise_and(image,image, mask= mask)            

cv2.imwrite('mask.jpg',mask)


cv2.imshow("mask ",mask)
cv2.imshow('stack', np.hstack([image, res]))
cv2.waitKey(0)


