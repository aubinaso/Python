# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 23:04:33 2021

@author: aubin
"""

import cv2 as cv
import numpy as np

img = cv.imread("lena.png")
cv.imshow("Image", img)

blank = np.zeros(img.shape, dtype='uint8')
#cv.imshow("black", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("gray", gray)

blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
#cv.imshow("blur", blur)

canny = cv.Canny(img, 125, 175)
#cv.imshow("canny",canny)

# binarise an image, every pixel below to 125 will be set to black and up will be set to 255
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0,0,255), 1)
#blank = où dessiner l'image (qu'elle matrice)
#contours = l'ensemble des contours
#1 = la largeur du dessin
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)