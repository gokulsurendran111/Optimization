# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 13:26:32 2022

@author: Nikhil
"""
import numpy as np
import matplotlib.pyplot as plt 

from radius_calc_final import *

reg_limit = [1000.0, 1000.0]
gamma = 100

Ndrones = 2

X = [566.31342767, 640.37890603, 406.10269162, 448.99945485,147.00716358, 453.84573556]

Dloc = np.zeros((Ndrones,3))
Dloc[0] = X[0:3]
Dloc[1] = X[3:6]
#    Dloc[2] = X[6:9]
#    Dloc[3] = X[9:12]
#    Dloc[4] = X[12:15]
#    Dloc[5] = X[15:18]

R = np.zeros(Ndrones)
for k in range(Ndrones):
    R[k] = calc_radius(Dloc[k], gamma, reg_limit)

for k in range(100):
    Jhist = []
    NPMC_list = [10, 10**2, 10**3, 10**4, 10**5, 10**6]
    for NPMC in NPMC_list:
    
        NP_inside = 0
        xp_mc = []
        yp_mc = []
        for inp in range(NPMC):
            xp = np.random.uniform(0,reg_limit[0])
            yp = np.random.uniform(0,reg_limit[1])
            if (point_in_coverage(xp,yp,Dloc,R) == 1):
                NP_inside = NP_inside + 1
                xp_mc.append(xp)
                yp_mc.append(yp)
    
        Jvalue = 1-NP_inside/NPMC 
        Jhist.append(Jvalue)
#        print(Jvalue)
    
    plt.plot(NPMC_list, Jhist, "o-")
    plt.xscale('log')
    plt.pause(0.01)
    plt.show()