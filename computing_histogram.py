# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 01:35:26 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lena.png")
cv.imshow("image", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)
# GrayScale histogram
# grayList = cv.calcHist([gray], [0], masked, [256], [0, 256])
# plt.figure()
# plt.title('GrayScale Histogram') 
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(grayList)
# plt.xlim([0,256])
# plt.show()

# Color Histogramme

plt.figure()
plt.title('Colour Histogram') 
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)