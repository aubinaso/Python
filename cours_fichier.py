# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:33:58 2020

@author: aubin
"""

import os
os.chdir("C:/Users/aubin/Projet_Python")

mon_fichier = open("fichier", "w")
print(mon_fichier)

mon_fichier.write("Bonjour je m'appelle Aubin")
mon_fichier.write("\nc'est comment aubin")

mon_fichier.close()

mon_fichier = open("fichier", "r")
contenu = mon_fichier.read()

print(contenu)
mon_fichier.close()

with open("fichier", "a") as mon_fichier:
    mon_fichier.write("\nça marche")
with open("fichier", "r") as mon_fichier:
    contenu = mon_fichier.read()
print(contenu.upper())