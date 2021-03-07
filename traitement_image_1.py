# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 10:30:51 2021

@author: aubin
"""
#bibliothèque de gestion des images python
import cv2 as cv
#lire une image dans une matrice
matrice = cv.imread("Lena.png")
#afficher les dimensions de l'image
print(matrice.shape)
print(matrice[0,0])
#convertir une image en Gray
"""matG = cv.cvtColor(matrice, cv.COLOR_BGR2GRAY)
print(matG.shape)
print(matG[0,0])"""

#lire une image dans une matrice en gray
matG = cv.imread("Lena.png", 0)
#enrégistrer une matrice
cv.imwrite("resultat.jpg", matG)
#afficher une matrice
cv.imshow("Image de matG", matG)
cv.waitKey(0)
cv.destroyAllWindows()