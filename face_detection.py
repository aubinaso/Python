# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:49:27 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# detect if there is a face not whose face it is which is face recognition
# https://github.com/opencv/opencv/tree/master/data/haarcascades

img = cv.imread("test.png")
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# read the xml file
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# return the rectangle cornet of the face, minNeighbors and scaleFactor increase the detection of face
# but more minNeighbors
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# print the number of faces found 
print("the number of face is ", len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow("Detected Faces", img)


cv.waitKey(0)