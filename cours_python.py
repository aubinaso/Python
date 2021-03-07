# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:45:02 2020

@author: aubin
"""

def afficherFlottant(flottant):
    string = str(flottant)
    partieR = string.split(".")[0]
    partieI = string.split(".")[1]
    return partieR, partieI
a,b = 0,0
try:
    chaine = input("entrer un flottant")
    flottant = float(chaine)
    a,b = afficherFlottant(flottant)
except:
    print("ce n'était pas un flottant")
finally:
    print("La partie réelle est {0} et la partie imaginaire est {1}".format(a, b))
liste2 = list()
liste2 = [1,2,3,4,5,6,7,8,9,0]

liste = [nb for nb in range(20) if nb%2==0]
print(liste)

mon_dictionnaire = dict()
mon_dictionnaire["pseudo"] = "aubinaso"
mon_dictionnaire["mot_de_passe"] = "mot2p@55e"
print(mon_dictionnaire)
print(mon_dictionnaire["pseudo"])
for cle in mon_dictionnaire.items() :
    print("{0} => {1}".format(cle[0], cle[1]))