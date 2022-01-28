import numpy as np
import math

from constraints import *

Nusers = 50
Ndrones = 6
User_Connection_status = np.zeros((Nusers, Ndrones))
Rmax = 400 # m
gamma = 110


DroneLoc=np.zeros((Ndrones,3))
for i in range(Ndrones):
    x = np.random.uniform(0,1000)
    y = np.random.uniform(0,1000)
    z = np.random.uniform(100,500)
    DroneLoc[i] = [x,y,z]



def cost(UserLoc, DroneLoc):
    
    for i in range(Nusers):
        for j in range(Ndrones):
            PLij = pathloss(DroneLoc[j], UserLoc[i])
#            print(PLij)
            dist = DroneUser_Distance(DroneLoc[j], UserLoc[i])
            if PLij <= gamma and dist <= Rmax:
                User_Connection_status[i,j] = 1
            elif PLij >= gamma or dist > Rmax:
                User_Connection_status[i,j] = 0
    
    ret = 0
    for i in range(Nusers):
        ret = ret + np.max(User_Connection_status[i,:])
        
#    print(ret)
    return ret

#cost(UserLoc, DroneLoc)

# x1 = np.linspace(0,1001,100)
# y1 = np.linspace(0,1001,100)
# check=[]

# karr = range(10000)
# for k in karr:
#     for i in range(Ndrones):
#         x = np.random.uniform(0,1000)
#         y = np.random.uniform(0,1000)
#         z = np.random.uniform(100,Rmax)
#         DroneLoc[i] = [x,y,z]
#     costval = cost(UserLoc, DroneLoc)
# #    print(costval)
#     check.append(costval)
# plt.plot(karr, check)


#for i in range(len(x1)):
#    DroneLoc[1,0] = x1[i]
#    costvalue=[]
#    for j in range(len(y1)):
#        DroneLoc[1,1] = y1[j]
#        costvalue = cost(UserLoc, DroneLoc)
#        check[i,j] = costvalue
#
#lenx1=len(x1)
#[X, Y] = np.meshgrid(x1,y1)
# 
#ax = plt.axes(projection ="3d")
#ax.plot_surface(X, Y, check, cmap = plt.cm.coolwarm) 
##ax.plot_wireframe(X, Y, check, color='k', linewidth=0.2) 
##fig, ax = plt.subplots(1, 1)
##ax.contourf(X,Y,check)
#  
#ax.set_title('Filled Contour Plot')
#ax.set_xlabel('feature_x')
#ax.set_ylabel('feature_y')