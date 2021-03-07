# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 21:10:36 2021

@author: aubin
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("lena.png")
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)
# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)