# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 00:12:26 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("Lena.png")

cv.imshow("Image de matG", image)
cv.waitKey(0)
cv.destroyAllWindows()

image = 255-image

cv.imshow("Image de matG", image)
cv.waitKey(0)
cv.destroyAllWindows()
#image = cv.imread("Lena.png")
#for i in range(0, image.shape[0]):
#   image[i, 100] = [255, 255, 255]

for i in range(0, image.shape[0]//2):
    for j in range(image.shape[1]//2):
        image[i,j,0] = 0
        
for i in range(0, image.shape[0]//2):
    for j in range(image.shape[1]//2, image.shape[1]):
        image[i,j,1] = 0
for i in range(image.shape[0]//2, image.shape[0]):
    for j in range(0, image.shape[1]//2):
        image[i,j,2] = 0

for i in range(image.shape[0]//2, image.shape[0]):
    for j in range(image.shape[1]//2, image.shape[1]):
        image[i,j,2] = 0
        image[i,j,1] = 0

cv.imshow("Image de matG", image)
cv.waitKey(0)
cv.destroyAllWindows()