# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 23:34:44 2022

@author: gokul
"""
import numpy as np
import math

from constraints import *
from terrain_popu import *

Nusers = 50
Ndrones = 5
User_Connection_status = np.zeros(Nusers)
Rmax = 400 # m
gamma = 100


DroneLoc=np.zeros((Ndrones,3))
for i in range(Ndrones):
    x = np.random.uniform(0,1000)
    y = np.random.uniform(0,1000)
    z = np.random.uniform(100,500)
    DroneLoc[i] = [x,y,z]

W=np.ones(Nusers)

def cost(DroneLoc,UserLoc):
    cos_val=0
    Ndrones=len(DroneLoc)
    Nusers=len(UserLoc)
 
    User_Connection_status = np.zeros(Nusers)

    for j in range(Ndrones):
        for i in range(Nusers):
            PLij = pathloss(DroneLoc[j], UserLoc[i])
            # print(PLij)
            if PLij <= gamma and User_Connection_status[i]==0:
                User_Connection_status[i] = 1
                cos_val += PLij/W[i]
                # print('connected')
            elif PLij>gamma:
                cos_val += PLij/W[i]
                # print('not connected')
            elif PLij <= gamma and User_Connection_status[i]==1:
                cos_val += 120
    print(np.sum(User_Connection_status))
                
    return cos_val

costval=[]
x=range(0,1000,10)
for i in x:
    DroneLoc[1,1]=i
    coss=cost(DroneLoc,UserLoc)
    costval.append(coss)
    
   
plt.plot(x,costval)




