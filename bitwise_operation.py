# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 01:12:36 2021

@author: aubin
"""

import cv2 as cv
import numpy as np
blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

# bitwise and => retourne l'intersection des deux images (avec 1)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise and", bitwise_and)

# bitwise or -> intersection region and not intersection region
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise or", bitwise_or)

# bitwise xor --> non intersecting region
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise xor", bitwise_xor)

# bitwise not -> inverse les bits : de noir à blanc et inverse
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise not", bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()