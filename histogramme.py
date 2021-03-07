# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 01:00:46 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("Lena.png")
b,v,r = cv.split(image)
y = 0.299*r + 0.587*v + 0.114*b
y = y.astype(np.uint8)

hist = np.zeros(256, int)
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        hist[y[i,j]] = hist[y[i,j]] + 1
    
plt.plot(hist)
plt.show()

hc = np.zeros(256, int)
hc[0]= hist[0]
for i in range(1, 256):
    hc[i] = hist[i] - hc[i-1]
    
nbpixels = y.size
hc = hc / nbpixels * 255
print(hc)

for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        y[i,j]=hc[y[i,j]]
cv.imshow("Luminance Y", y)
cv.waitKey(0)
cv.destroyAllWindows()