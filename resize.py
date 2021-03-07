# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 02:27:08 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lena.png")
cv.imshow("originale", img)
cv.waitKey(0)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

image = rescaleFrame(img)
cv.imshow("modified", image)
cv.waitKey(0)