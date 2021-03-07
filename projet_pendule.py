# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 00:05:05 2020

@author: aubin
"""

"""def inc():
    global i
    i += 1
    
i = 4
print(i)
inc()
print(i)"""
import pickle
import os
import random
os.chdir("C:/Users/aubin/Projet_Python")

def choixMot(liste_m):
    liste = list(liste_m)
    random.shuffle(liste)
    """i = random.randint(0, len(liste))"""
    val = liste[0]
    return val

liste_mot = list()
try:
    with open("fichier_mot", "rb") as mon_fichier:
        try:
            mon_depickler = pickle.Unpickler(mon_fichier)
            liste_mot = mon_depickler.load()
        except:
                print("...")
except:
    print("...")
    
dict_victoire = dict()
try:
    with open("fichier_victoire", "rb") as mon_fichier:
        try:
            mon_depickler = pickle.Unpickler(mon_fichier)
            dict_victoire = mon_depickler.load()
        except:
            print("...")
except:
    print("...")
    
nom = input("entrer votre nom\n")
i = 0
while(i == 0):
    i = 1
    try:
        chaine = input("entrer la chaine en minuscule à ajouter\n")
        assert(len(chaine)<8)
        liste_mot.append(chaine.lower())
    except:
        print("la chaine doit être inférieur ou égale à 8 caractères")
    try:
        i = int(input("Voulez vous ajouter une chaine pas plus de 8 caractères?? '0' -> 'Oui' && '1' -> 'Non'\n"))
    except:
        print("entrer '0' -> 'Oui' && '1' -> 'Non'")
        
print(liste_mot)
random.shuffle(liste_mot)
print(liste_mot)
i = random.randint(0, len(liste_mot)-1)
print(i)
val_a_trouver = liste_mot[i]
val_trouver = "..................."[:len(val_a_trouver)]
list_trouver = list([a for a in val_trouver])
i = 1
a = 1
while a == 1 :
    print("voici votre mot",val_trouver)
    c = input("entrer un caractère si plus juste le premier caractère sera pris en compte\n")[:1]
    """trouve = lambda val_a_trouver, c: [y for y, val in enumerate(val_a_trouver) if val == c]"""
    trouve = list()
    for y, val in enumerate(val_a_trouver):
        if val == c:
            print(y)
            trouve.append(int(y))
    print(trouve)
    for elt in trouve:
        """val_trouver.insert(y, c)
        del val_trouver[y+1]"""
        list_trouver[elt] = c
        val_trouver = "".join(list_trouver)
    if "." not in list_trouver:
        a=0
    if i> 8:
        a=0
    
    
    
score = 0
if val_trouver == val_a_trouver:
    score = 1
try:
    dict_victoire[nom] = dict_victoire[nom] + score
except:
    dict_victoire[nom] = 0

print(dict_victoire)

with open("fichier_mot", "wb") as mon_fichier:
    mon_pickler = pickle.Pickler(mon_fichier)
    mon_pickler.dump(liste_mot)

with open("fichier_victoire", "wb") as mon_fichier:
    mon_pickler = pickle.Pickler(mon_fichier)
    mon_pickler.dump(dict_victoire)