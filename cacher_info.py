# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 01:55:19 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("lena.png")
message = cv.imread("message.png", 0)

dsize = (330, 330)
message = cv.resize(message, dsize)

b,v,r = cv.split(image)
b=b & 0b11111110
b = b | (message > 0)

cache = cv.merge((b,v,r))
cv.imwrite("cache.png", cache)

cv.imshow("Image de matG", cache)
cv.waitKey(0)
cv.destroyAllWindows()

b,v,r = cv.split(image)
cache = (b & 1)^(v & 1)
cache = cache * 255.0

cv.imshow("contenu caché", cache)
cv.waitKey(0)
cv.destroyAllWindows()