# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:48:07 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as ptl

blank = np.zeros((500, 500, 3), dtype="uint8")
blank[200:300,:] = (0,255,0)

cv.putText(blank, 'Hello Aubin', (0,255), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (255,0,0),2)

#convert an image to a gray style
gray = cv.cvtColor(blank, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#Blur an image : rendre floue => le (7,7) détermine l'intensité de floutage
blur = cv.GaussianBlur(blank, (7,7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

#Edge Cascade : enlève toute couleur et transforme une image en dessin
canny = cv.Canny(blank, 125,175)
cv.imshow("Edge cascade", canny)

#dilating image
dilate = cv.dilate(canny, (3,3), iterations=4)
cv.imshow("dilating image", dilate)

#Eroding dilate image
erode = cv.erode(dilate, (3,3), iterations=4)
cv.imshow("erode", erode)

#Resizing
resize = cv.resize(blank, (200,200), interpolation=cv.INTER_AREA)#interpolations pour avoir une bonne image
#inter_area => inter_linear => inter_cubic (lent mais meilleur qualité)
cv.imshow("resize", resize)

# Cropping : une partie de l'image
cropping = blank[20:200, 200:400]
cv.imshow("Cropping", cropping)

cv.imshow('Blank', blank)
cv.waitKey(0)
cv.destroyAllWindows()