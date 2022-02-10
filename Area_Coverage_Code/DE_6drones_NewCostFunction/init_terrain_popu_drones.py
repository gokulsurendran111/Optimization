import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

terrain_x=np.loadtxt("xData.txt",dtype='float')
terrain_y=np.loadtxt("yData.txt",dtype='float')
terrain_z=np.loadtxt("zData.txt",dtype='float')
UserLoc=np.loadtxt("population.txt",dtype='float')

UsersOnHill = UserLoc[UserLoc[:,2] > 10.0]
User_Weights = np.ones(len(UserLoc))
User_Weights[UserLoc[:,2] > 10.0] = np.full(len(UsersOnHill),10.0)

## Drone Characteristics
Nusers = len(UserLoc) # 50
Ndrones = 6
gamma = 100
Rmax = 500#np.power(10,90.0/20)*299792458.0/(4*np.pi*2.0e9)

## Generation of User Weights. Weightage given to all users on the hill

""" Old Method to give User Weights 
box_y_min = 0.0
box_y_max = 200.0
box_x_min = 800.0
box_x_max = 1000.0

for i in range(len(UserLoc)):
    xuser = UserLoc[i,0]
    yuser = UserLoc[i,1]
    if ( xuser < box_x_max ) and ( xuser > box_x_min ):
        if ( yuser < box_y_max ) and ( yuser > box_y_min ):
            User_Weights[i] = 2.0
"""
