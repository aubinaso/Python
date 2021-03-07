# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 00:53:04 2021

@author: aubin
"""

import cv2 as cv
import numpy as np

img = cv.imread("lena.png")
cv.imshow("tof", img)

# Averaging Blur
average = cv.blur(img, (3,3))
cv.imshow("average", average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("gaussing", gaussian)

# Median Blur => bon blur
median = cv.medianBlur(img, 3)
cv.imshow("median", median)

# Bilateral Blur => meilleur blur
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)