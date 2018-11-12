# -*- coding: utf-8 -*-
"""Test Ex 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Jgfg6gQnHUI--pKuBCKTZl8G5QlfYXj

Pas eu le temps de finir le programme malheureusement.

## Importer les outils
"""

# vecteurs et algèbre linéaire
import numpy as np

# les outils pour visualiser
import matplotlib.pyplot as plt

# le solveur
import scipy.integrate as solveur

"""## Définir les constantes du problème"""

k1 = 4.17E-3 #mol/L*s
k2 = 1.65E-3 #mol/L*s
k3 = 8.33E-2 #mol/L*s
CA0 = 1.5 # mol/L
CB0 = 2 # mol/L
CC0 = 0 # mol/L
CD0 = 0
CE0 = 0
CF0 = 0
V = 50 # L
Vd = 0.167 #L/s

"""## Définir les équations à résoudre"""

def equations(variables, v, Vd):
    FA, FB, FC = variables
    
    r1 = k1*CA*CB
    r2 = k2*CA*CD
    r3 = k3*CB^2*CC
    
    FA0 = CA0*Vd
    FB0 = CB0*Vd
  
    RA = -r1-3*r2
    RB = 2*r1-r3
    RC = r1+r2-2*r3
    RD = r1-2*r2+r3
    RE = r2
    RF = r3
    
    dFAdv = RA
    dFBdv = RB
       
    return dFAdv, dFBdv, dFCdv

"""## Définir les conditions initiales"""

conditions_initiales = [CA0 * Vd, CB0 * Vd]

"""## Résoudre le problème à l'aide du solveur"""

v = np.linspace(0, 50, 1000) # définir les bornes d'intégration

resultats = solveur.odeint(equations, conditions_initiales, v, (V, Vd))

FC = resultats[:,0]

FC0 = 0
X = (FC0 - FC) / FC0

"""## Visualiser les résultats"""

plt.plot(v, X)
plt.xlabel('t')
plt.ylabel('X (-)')
plt.legend(['X'])
plt.show()

t[X > 0.3][0]
