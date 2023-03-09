# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:07:04 2022

@author: karak
"""


# importing opencv
import cv2
 
# reading the images
circle = cv2.imread('test1.jpg')
star = cv2.imread('test.jpg')
 
# subtract the images
subtracted = cv2.subtract(star, circle)
 
# TO show the output
cv2.imshow('image', subtracted)
cv2.imwrite('black.jpg',subtracted)
# To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()