import numpy as np
import math

from constraints import *
from terrain_popu import *

Nusers = len(UserLoc)
Ndrones = len(DroneLoc)
User_Connection_status = np.zeros((Nusers, Ndrones))
Rmax = 100 # m

def cost(UserLoc, DroneLoc):
    
    for i in range(Nusers):
        for j in range(Ndrones):
            PLij = pathloss(DroneLoc[j], UserLoc[i])
            dist = DroneUser_Distance(DroneLoc[j], UserLoc[i])
            if PLij < 200 and dist <= Rmax:
                User_Connection_status[i,j] = 1
            elif PLij>=200 or dist>Rmax:
                User_Connection_status[i,j] = 0
    
    ret = 0
    for i in range(Nusers):
        ret = ret + np.max(User_Connection_status[i,:])
        
    # print(ret)
    return ret

costvalue = cost(UserLoc, DroneLoc)
#
x1 = np.linspace(0,1000,1000)
check = []
for x in x1:
    DroneLoc[4,0] = x
    # print(DroneLoc[0])
    costvalue = cost(UserLoc, DroneLoc)
    check.append(costvalue)
                
plt.plot(x1, check)