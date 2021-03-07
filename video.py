# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 02:15:31 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

video = cv.VideoCapture(0) # li au travers de la camera
#video = cv.ViedoCapture('Aubin.mp4')
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = video.read()
    frame_resized = rescaleFrame(frame)
    frame_resize = cv.Canny(frame_resized, 125, 175)
    frame_blur = cv.GaussianBlur(frame_resized, (3,3), cv.BORDER_DEFAULT)
    
    cv.imshow('Video', frame_resized)
    cv.imshow('edge', frame_resize)
    cv.imshow('blur', frame_blur)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.waitKey(0)
cv.destroyAllWindows()