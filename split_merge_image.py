# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 00:39:01 2021

@author: aubin
"""

import cv2 as cv
import numpy as np

img = cv.imread("lena.png")
cv.imshow("image", img)

b,g,r = cv.split(img)

# cv.imshow("blue", b)
# cv.imshow("green", g)
# cv.imshow("red", r)

merged = cv.merge([b,g,r])
cv.imshow("merged", merged)

blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
cv.imshow("blue", blue)
green = cv.merge([blank,g,blank])
cv.imshow("green", green)
red = cv.merge([blank,blank,r])
cv.imshow("red", red)

cv.waitKey(0)