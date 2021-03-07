# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 01:24:45 2021

@author: aubin
"""

import cv2 as cv
import numpy as np

img = cv.imread("lena.png")
cv.imshow("image", img)

#the dimension of the mask has to be the same as the image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked image", masked)

cv.waitKey(0)