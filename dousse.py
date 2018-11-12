# -*- coding: utf-8 -*-
import numpy as np #pour les arrays
import matplotlib.pyplot as plt #pour les plots
import scipy.integrate as integ #pour intégrer

#Ne pas oublier les unités en commentaires!
CA0 = 1.5 #mol/L
CB0 = 2 #mol/L
Vdot = 10 #L/min

def equations(var, V): #Définir les équations à résoudre, on peut devoir ajouter ",a ,b, c, d"
    FA, FB, FC, FD, FE, FF = var
    
    CA = FA / Vdot
    CB = FB / Vdot
    CC = FC / Vdot
    CD = FD / Vdot
    
    r1 = 0.25 * CA * CB
    r2 = 0.1 * CA * CD
    r3 = 5 * (CB**2) * CC
    
    RA = -r1 -3*r2
    RB = -2*r1 - r3
    RC = r1 + r2 - 2*r3
    RD = r1 - 2*r2 + r3
    RE = r2
    RF = r3
    
    dFAdV = RA 
    dFBdV = RB
    dFCdV = RC
    dFDdV = RD 
    dFEdV = RE
    dFFdV = RF 
    
    return dFAdV, dFBdV, dFCdV, dFDdV, dFEdV, dFFdV

conditions_initiales = [CA0*Vdot, CB0*Vdot, 0, 0, 0, 0] #Définir les conditions initiales

V = np.linspace(0,50,10000) #Ou np.linspace(floor, ceiling, increment), définition des bornes d'intégration
results = integ.odeint( #On donne la fonction, les conditions initiales et les bornes.
        equations,
        conditions_initiales,
        V
        ) 

"""Calculer X"""
FA = results[:,0]

FA0 = CA0*Vdot
X = (FA0-FA)/FA0

print(X[V==50])


"""Cercher CC à V=50"""
FC = results [:,2]
CC = FC/Vdot

print(CC[V==50])

"""plot"""
plt.figure(1)
plt.plot(V,results)
plt.xlabel('V [L]')
plt.ylabel('FA, FB, FC, FD, FE, FF [mol/min]')
plt.legend(['FA', 'FB', 'FC', 'FD', 'FE', 'FF'])
plt.show