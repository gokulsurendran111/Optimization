import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

terrain_x=np.loadtxt("xData.txt",dtype='float')
terrain_y=np.loadtxt("yData.txt",dtype='float')
terrain_z=np.loadtxt("zData.txt",dtype='float')
UserLoc=np.loadtxt("population.txt",dtype='float')

terrain = terrain_z

fig = plt.figure(1)
ax = plt.axes(projection ="3d")
ax.set_zlim([0,300])

ax.plot_wireframe(terrain_x, terrain_y, terrain_z, color='k', linewidth=0.2)

ax.set_xlabel("Horizontal X axis (m)")
ax.set_ylabel("Horizontal Y axis (m)")
ax.set_zlabel("Altitude (m)")
ax.scatter3D(UserLoc[:,0], UserLoc[:,1], UserLoc[:,2], marker='o', color='r', s=20)
plt.show()

User_Weights = np.ones(len(UserLoc))

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
            
