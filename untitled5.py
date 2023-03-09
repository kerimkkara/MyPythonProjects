# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:23:24 2022

@author: karak
"""

import cv2
import numpy as np

image = cv2.imread('blackeroz.jpg')
# image = cv2.blur(image,(3,3))
# image = cv2.medianBlur(image, 3)

kernel = np.ones((1,1),np.uint8)
image = cv2.erode(image,kernel,iterations = 2)

kernel = np.ones((2,2),np.uint8)
image = cv2.dilate(image,kernel,iterations = 2)

kernel = np.ones((2,2),np.uint8)
image = cv2.erode(image,kernel,iterations = 2)

kernel = np.ones((4,4),np.uint8)
image = cv2.dilate(image,kernel,iterations = 1)

kernel = np.ones((3,3),np.uint8)
image = cv2.erode(image,kernel,iterations = 2)


# kernel = np.ones((2,2),np.uint8)
# image = cv2.erode(image,kernel,iterations = 1)
        

cv2.imwrite('blackeroz2.jpg',image)
cv2.imshow("mask ",image)
cv2.waitKey(0)