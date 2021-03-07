# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:39:15 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lena.png")
cv.imshow("Image", img)
gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
cv.imshow("gray", gray)

# Simple Thresholding => threshold will have 150 => and thresh will have the image return
threshold, thresh = cv.threshold(gray, 110, 255, cv.THRESH_BINARY)
cv.imshow("simple threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 110, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple threshold Inverse", thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow("Adaptive thresholding", adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adaptive thresholding Inverse", adaptive_thresh_inv)




cv.waitKey(0)