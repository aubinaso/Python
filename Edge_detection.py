# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:12:07 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lena.png")
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Combined Sobel", combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow("canny", canny)

cv.waitKey(0)