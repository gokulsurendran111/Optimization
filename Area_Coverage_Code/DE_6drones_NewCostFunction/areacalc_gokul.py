# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 01:38:09 2022

@author: gokul
"""

import numpy as np
from radius_calc_final import *
from constraints import *
from terrain_popu import *
import time


reg_limit = [1000.0, 1000.0]
gamma = 100
Rmax = 500
Ndrones=6
np.random.seed(0)
Nusers = len(UserLoc)
Dloc_Array=np.random.uniform(0,500,18) 
Dloc = np.zeros((Ndrones,3))
Dloc[0] = Dloc_Array[0:3]
Dloc[1] = Dloc_Array[3:6]
Dloc[2] = Dloc_Array[6:9]
Dloc[3] = Dloc_Array[9:12]
Dloc[4] = Dloc_Array[12:15]
Dloc[5] = Dloc_Array[15:18]

#############################################################
### Area calc by Nikhil sir's code

R = np.zeros(Ndrones)
for k in range(Ndrones):
    R[k] = calc_radius(Dloc[k], gamma, reg_limit)
    
start1=time.time()
 
NP_inside = 0
NPMC = 50000
xp_mc = []
yp_mc = []
for inp in range(NPMC):
    xp = np.random.uniform(0,reg_limit[0])
    yp = np.random.uniform(0,reg_limit[1])
    if (point_in_coverage(xp,yp,Dloc,R) == 1):
        NP_inside = NP_inside + 1
        xp_mc.append(xp)
        yp_mc.append(yp)

Area_not_covered = 1-NP_inside/NPMC 


end1=time.time()

###########################################################

###########################################################

#Area calc after vectorization ############################

start2=time.time()

NPMC=50000

for i in range(100):
    xp1 = np.random.uniform(0,reg_limit[0],50000)
    yp1 = np.random.uniform(0,reg_limit[1],50000)
    Np_inside1=point_in_coverage1(xp1,yp1,Dloc,R)
    Area_cov=np.sum(Np_inside1)
    xp_mc1=xp1[Np_inside1]
    yp_mc1=yp1[Np_inside1]

Area_not_covered1 = 1-Area_cov/NPMC 
    

end2=time.time()






