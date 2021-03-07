# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 02:02:56 2020

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
            
bernard = Personne("Bernard", 14, "Gabriel", "Paris")
jean = Personne("Jean", 15, "Jacques", "Troyes")

print(bernard.nom, bernard.prenom, "a", bernard.age, "ans", "et vie à", bernard.residence)
print(jean.nom, jean.prenom, "a", jean.age, "ans", "et vie à", jean.residence)
print("le nombre de personne est",Personne.compteur)
bernard.marcher()

class TableauNoir:
    """classe du tableau
        -surface"""
    nombre_de_tableau = 0   
    def combien(cls):
        print("il y'a", TableauNoir.nombre_de_tableau)
    
    combien = classmethod(combien)
    
    def afficher():
        print(TableauNoir.nombre_de_tableau)
        
    afficher = staticmethod(afficher)
        
    def __init__(self):
        TableauNoir.nombre_de_tableau += 1
        self.surface = ""
        self.nombre_ecrire = 0
    
    def effacertableu(self):
        self.surface = ""
        self.nombre_ecrire = 0
    
    def ecrire(self, meessage_a_ecrire):
        if(self.nombre_ecrire >= 3):
            print(self.surface)
            print("\n\n\tNous effaçons le tableau")
            self.effacertableu()
        if(self.surface != ""):
            self.surface += "\n"
        self.surface += meessage_a_ecrire
        self.nombre_ecrire += 1
    
    def lire(self):
        print(self.surface)


        
tableau = TableauNoir()
tableau.ecrire("bonjour")
TableauNoir.ecrire(tableau, "bon")
TableauNoir.lire(tableau)
print("relire")
tableau.lire()
tableau.combien()
TableauNoir.combien()
TableauNoir.afficher()
dir(tableau)
tableau.__dict__

