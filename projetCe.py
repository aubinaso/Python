# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:32:40 2020

@author: aubin
"""

import random
import math
import time

def genereVal():
    val = random.random()
    return val

def genereval(min, max):
    val = random.uniform(min, max)
    return val

def calculTi(i):
    val = math.log10(i)/beta
    val = math.fabs(val)
    return val

def calculErreur(somme1, n, T):
    Ttheo = somme1 / n
    val = Ttheo - T
    val = math.fabs(val)
    val = val / T
    return val

beta = 0.5
T = 1/beta
Tcalcul = 0
sommecalcul = 0
somme = 0
valgenere = 0
n = 0
alpha = 0.01
alphacalcul = 1
min0 = 0
max0 = 0
while alphacalcul >= alpha:
    n += 1
    valgenere = genereVal()
    ti = calculTi(valgenere)
    if n > 1 and calculErreur(sommecalcul + ti, n, T) > alphacalcul:
        if (sommecalcul + ti)/n > T:
            max0 = math.pow(10, beta*(sommecalcul - n*T*(alphacalcul + 1)))
            valgenere = genereval(0, max0)
            ti = calculTi(valgenere)
        else:
            min0 = math.pow(10, beta*(-n*T*(alphacalcul - 1) + sommecalcul))
            max0 = math.pow(10, beta*(n*T*(alphacalcul - 1) - sommecalcul))
            valgenere = genereval(min0, max0)
            ti = calculTi(valgenere)
    
    sommecalcul += ti
    somme = T*n
    Tcalcul = sommecalcul/n
    """print("la valeur Tcalcul est {0} et la valeur T est {1}".format(Tcalcul, T))
    print("la somme est {0} et la somme statistique est {1}".format(somme, sommecalcul))"""
    alphacalcul = math.fabs((Tcalcul - T)/T)
    """print("l'erreur est ",alphacalcul, " au lieu de ", alpha)
    time.sleep(5)"""
print("n vaut ", n)
    