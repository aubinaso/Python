# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:39:53 2020

@author: aubin
"""

import pickle


score = {"pseudo" : "aubinaso", "mot_de_passe" : "m0t2p@55e", "email" : "takamtayoaubinpatrick@gmail.com"}

with open("donnees", "wb") as mon_fichier:
    mon_pickle = pickle.Pickler(mon_fichier)
    mon_pickle.dump(score)
    
with open("donnees", "rb") as mon_fichier:
    mon_depickler = pickle.Unpickler(mon_fichier)
    score_recupere = mon_depickler.load()
print(score_recupere)