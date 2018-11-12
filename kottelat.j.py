#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# importation des modules manquants

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as solver

# Définition des constantes
Vdot = 10 # L/min

FA0 = 1.5*Vdot # mol/min
FB0 = 2*Vdot   # mol/min
FC0 = 0   # mol/min
FD0 = 0   # mol/min
FE0 = 0   # mol/min
FF0 = 0   # mol/min


# Définition des équations différentielles

def equations(variables_dependantes, V, Vdot):
    # définition des variables
    # variable indépendente : V
    # variables dépendantes : FA, FB, FC, FD, FE, FF
    
    FA, FB, FC, FD, FE, FF = variables_dependantes
    
    # équations différentielles
    CA = FA/Vdot # mol/L
    CB = FB/Vdot # mol/L
    CC = FC/Vdot # mol/L
    CD = FD/Vdot # mol/L
    CE = FE/Vdot # mol/L (inutile)
    CF = FF/Vdot # mol/L (inutile)
    
    r1 = 0.25*CA*CB # mol/L/min
    r2 = 0.1*CA*CD  # mol/L/min
    r3 = 5*CB**2*CC # mol/L/min
    
    RA = -r1-3*r2   # mol/L/min
    RB = -2*r1-r3   # mol/L/min
    RC = r1+r2-2*r3 # mol/L/min
    RD = r1-2*r2+r3 # mol/L/min
    RE = r2         # mol/L/min
    RF = r3         # mol/L/min
    
    dFAdV = RA # mol/L/min
    dFBdV = RB # mol/L/min
    dFCdV = RC # mol/L/min
    dFDdV = RD # mol/L/min
    dFEdV = RE # mol/L/min
    dFFdV = RF # mol/L/min
    
    return dFAdV, dFBdV,dFCdV, dFDdV, dFEdV, dFFdV

# Définition des conditions initiales
    
conditions_initiales = [FA0, FB0, FC0, FD0, FE0, FF0]

# Définition des limites d'intégration

V = np.linspace(0, 50, 51) # intégration du volume V entre 0 et 50 L

# Résoudre

resultats = solver.odeint(equations, conditions_initiales, V, (Vdot,))

# Graphique

plt.plot(V, resultats)
plt.grid()
plt.title('Evolution des F_i en fonction du volume')
plt.xlabel('V [L]]')
plt.ylabel('FA, FB, FC, FD, FE, FF [mol/min]')
plt.legend(['FA', 'FB', 'FC', 'FD', 'FE', 'FF'])
plt.show()

# Extraire les résultats

FA = resultats[:,0]
FC = resultats[:,2]

print('FA (V=50L) = ', FA[50])
print('\nFC (V=50L) = ',FC[50])