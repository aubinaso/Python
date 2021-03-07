# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 21:26:01 2021

@author: aubin
"""

import cv2 as cv
import numpy as np

img = cv.imread("lena.png")

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -X --> translate to the left
# X --> translate to the rigth
# -Y --> translate to Up
# Y --> translate down
translated = translate(img, 100, 0)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)

# Flipping 1 => flip horizontaly, 0 => flip verticaly, -1 => vertical and horizontal
flip = cv.flip(img, -1)
cv.imshow("Flip", flip)

cv.imshow("rotation", rotated)
cv.imshow("image", img)
cv.imshow('Translated', translated)
cv.waitKey(0)
