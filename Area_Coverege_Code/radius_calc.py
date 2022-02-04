# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 16:54:47 2022

@author: Nikhil
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import time

start = time.time()

def pathloss(Drone_coord, r):
    dx = Drone_coord[0]
    dy = Drone_coord[1]
    dz = Drone_coord[2]
    
    Delta_h = dz
    hor_dist = r
    dist = np.sqrt( Delta_h**2 + hor_dist**2 )
    
    theta = math.atan2(Delta_h , hor_dist)
    theta = np.rad2deg(theta)
    
#    a = 9.61 # Urban
#    b = 0.16
#    eta_LOS = 1.0
#    eta_NLOS = 20
    
    a = 12.08  # Dense Urban
    b = 0.11
    eta_LOS = 1.6
    eta_NLOS = 23    
    
    PLOS = 1.0/(1 + a*np.exp( -b*(theta - a) ))
    PNLOS = 1 - PLOS
    
    fc = 2.0*10**9
    c = 299792458.0
    
    PL = 20*np.log10(4*np.pi*fc*dist/c) + PLOS*eta_LOS + PNLOS*eta_NLOS
    return PL

def calc_radius(D1, gamma):

    x_lim = min(D1[0], reg_limit[0] - D1[0])
    y_lim = min(D1[1], reg_limit[1] - D1[1])
    r_lim = min(x_lim, y_lim)
    
    r_arr = np.linspace(0,1000,500)
    
    f1 = []
    for r in r_arr:
        pl = pathloss(D1, r)
        if pl < gamma:
            u = 1
        else:
            u = 0
        f1.append(u)
    
    for i in range(len(f1)):
        if f1[i] == 1:
            k = i
            
    radius = r_arr[k]
    return radius

def point_in_coverage(xp, yp, Dloc, R):
    ret = 0
    
    for i in range(len(R)):
        dist = np.sqrt( (xp - Dloc[i,0])**2 + (yp - Dloc[i,1])**2 )
        if dist < R[i]:
            ret = 1
            break
    
    return ret

def Area_intersection(D1, R1, D2, R2):
    
    d = np.sqrt( (D1[0] - D2[0])**2 + (D1[1] - D2[1])**2 )
    
    if ( d >= R1 + R2 ):
        Aint = 0
    elif ( d <= abs(R1 - R2) ):
        if (R1 < R2):
            Aint = np.pi*R1**2
        else:
            Aint = np.pi*R2**2
    else:
        d1 = (R1**2 - R2**2 + d**2)/(2*d)
        d2 = d - d1
        
        A1 = R1**2*np.arccos(d1/R1) - d1*np.sqrt( R1**2 - d1**2 )
        A2 = R2**2*np.arccos(d2/R2) - d2*np.sqrt( R2**2 - d2**2 )
        Aint = A1 + A2
    return Aint
    

D1 = [500.0, 500.0, 200.0]
reg_limit = [1000.0, 1000.0]
gamma = 100

Dloc = np.zeros((6,3))
for k in range(6):
    x = np.random.uniform(0,reg_limit[0])
    y = np.random.uniform(0,reg_limit[1])
    z = np.random.uniform(100, 500)
    Dloc[k] = [x,y,z]

#Dloc = np.zeros((6,3))
#Dloc[0] = [314.44311387, 725.4801989 , 323.44626112]
#Dloc[1] = [798.39703445, 936.72797249, 214.23306768]
#Dloc[2] = [864.98420553, 552.61242967, 303.34549943]
#Dloc[3] = [143.23023758,  83.96567213, 151.19966343]
#Dloc[4] = [558.44431935, 100.08121905, 152.17333412]
#Dloc[5] = [294.35096775, 159.23726942, 205.99114273]

"""
Jcost = 0

R = np.zeros(6)
A = np.zeros(6)
for k in range(6):
    R[k] = calc_radius(Dloc[k], gamma)
    A[k] = np.pi*R[k]**2
    Jcost = Jcost + A[k]

Aint_total = 0    
for i in range(6):
    for j in range(6):
        if (i != j):
            Aint = Area_intersection(Dloc[i], R[i], Dloc[j], R[j])
            Aint_total = Aint_total + Aint

Perc_covered = (Jcost-Aint_total)*100/(1000*1000)
print(Perc_covered)
"""

figure, axes = plt.subplots()

plt.plot([0,0],[0,1000],"k",linewidth=5)
plt.plot([0,1000],[0,0],"k",linewidth=5)
plt.plot([0,1000],[1000,1000],"k",linewidth=5)
plt.plot([1000,1000],[0,1000],"k",linewidth=5)

for i in range(6):
    plt.scatter(Dloc[i,0], Dloc[i,1], marker='s', color='b')
    c_filled = plt.Circle((Dloc[i,0], Dloc[i,1]), R[i], fill=True, alpha = 0.2)
    c_boundary = plt.Circle((Dloc[i,0], Dloc[i,1]), R[i], fill=False)
    axes.add_artist( c_filled )
    axes.add_artist( c_boundary )

NP_inside = 0
NPMC = 10000
xp_mc = []
yp_mc = []
for inp in range(NPMC):
    xp = np.random.uniform(0,reg_limit[0])
    yp = np.random.uniform(0,reg_limit[1])
    if ( point_in_coverage(xp,yp,Dloc,R) == 1):
        NP_inside = NP_inside + 1
        xp_mc.append(xp)
        yp_mc.append(yp)
#        plt.scatter(xp, yp, marker='.', color='r')

plt.scatter(xp_mc, yp_mc, marker='.', color='r')        
print(NP_inside/NPMC)


plt.xlim([-200,1200])
plt.ylim([-200,1200])
axes.set_aspect(1)
plt.show()

end = time.time()
print("Time : ", end - start)