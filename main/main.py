import numpy as np
import math

from constraints import *

Nusers = 50
Ndrones = 9
User_Connection_status = np.zeros((Nusers, Ndrones))
Rmax = 100 # m

def cost(UserLoc, DroneLoc):
    
    for i in range(Nusers):
        for j in range(Ndrones):
            PLij = pathloss(DroneLoc[j], UserLoc[i])
            dist = DroneUser_Distance(DroneLoc[j], UserLoc[i])
            if PLij < 200 and dist <= Rmax:
                User_Connection_status[i,j] = 1
            elif (User_Connection_status[i,j] != 1):
                User_Connection_status[i,j] = 0
    
    ret = 0
    for i in range(Nusers):
        ret = ret + np.max(User_Connection_status[i,:])
        
    print(ret)
    return ret

costvalue = cost(UserLoc, DroneLoc)
#
x1 = np.linspace(0,1000,100)
check = []
for x in x1:
    DroneLoc[4,0] = x
    costvalue = cost(UserLoc, DroneLoc)
    check.append(costvalue)
                
plt.plot(x1, check)