# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 23:34:44 2022

@author: gokul
"""
import numpy as np
import math

from constraints import *

Nusers = 50
Ndrones = 6
User_Connection_status = np.zeros(Nusers)
Rmax = 400 # m
gamma = 110


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
    print(Nusers)
    User_Connection_status = np.zeros(Nusers)
    print(User_Connection_status)
    for j in range(Ndrones):
        for i in range(Nusers):
            PLij = pathloss(DroneLoc[j], UserLoc[i])
            print(PLij)
            if PLij <= gamma and User_Connection_status[i]==0:
                User_Connection_status[i] = 1
                cos_val = cos_val + PLij/W[i]
            elif PLij>gamma and User_Connection_status[i]==0:
                cos_val = cos_val + PLij/W[i]
            print(cos_val)
                
                
    return cos_val
            # elif PLij >= gamma:
            #     User_Connection_status[i,j] = 0
    
#     ret = 0
#     for i in range(Nusers):
#         ret = ret + np.max(User_Connection_status[i,:])
        
# #    print(ret)
#     return ret