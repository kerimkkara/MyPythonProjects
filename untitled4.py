# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:16:23 2022

@author: karak
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('maskeroz.jpg')
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, output2) = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
output2 = cv2.GaussianBlur(output2, (5, 5), 3)
output2 = cv2.Canny(output2, 180, 255)
plt.imshow(output2)
plt.show()