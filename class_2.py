# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 11:59:46 2021

@author: aubin
"""

class Personne:
    """Classe définissant une personne caractérisée par
        - son nom
        - son prenom
        - son âge
        - son lieu de résidence"""
    compteur = 0
    def __init__(self, nom, age, prenom, residence):
        self.nom = nom
        self.age = age
        self.prenom = prenom
        self.residence = residence
        Personne.compteur += 1
        
    def marcher(self):
        print(self.nom," marche")
        
    def _get_residence(self):
        print("je suis entré")
        return self.residence

    def _set_residence(self, nouvelle_residence):
        print("on change de valeur")
        self.residence = nouvelle_residence
        
    residence = property(_get_residence, _set_residence)

            
bernard = Personne("Bernard", 14, "Gabriel", "Paris")
jean = Personne("Jean", 15, "Jacques", "Troyes")

print(bernard.nom, bernard.prenom, "a", bernard.age, "ans", "et vie à", bernard.residence)
print(jean.nom, jean.prenom, "a", jean.age, "ans", "et vie à", jean.residence)
print("le nombre de personne est",Personne.compteur)
bernard.marcher()