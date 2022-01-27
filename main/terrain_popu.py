import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

terrain_x=np.loadtxt("xData.txt",dtype='float')
terrain_y=np.loadtxt("yData.txt",dtype='float')
terrain_z=np.loadtxt("zData.txt",dtype='float')
UserLoc=np.loadtxt("population.txt",dtype='float')
# UserLoc=np.array([[495,435,5],[450,480,5],[999,999,999]])

terrain = terrain_z
DroneLoc=np.array([[100,100,terrain[100,100]+50],[300,300,terrain[300,300]+50],[500,500,terrain[500,500]+50],
                [300,700,terrain[300,700]+50],[100,900,terrain[100,900]+50],[700,300,terrain[700,300]+50],
                [700,700,terrain[700,700]+50],[900,100,terrain[900,100]+50],[900,900,terrain[900,900]+50]])

# DroneLoc=np.array([[500,50,55],[999,999,55]])



fig = plt.figure(1)
ax = plt.axes(projection ="3d")
ax.set_zlim([0,300])

ax.plot_wireframe(terrain_x, terrain_y, terrain_z, color='k', linewidth=0.2)

ax.scatter3D(UserLoc[:,0], UserLoc[:,1], UserLoc[:,2], marker='o', color='r', s=20)
ax.scatter3D(DroneLoc[:,0], DroneLoc[:,1], DroneLoc[:,2], marker='s', color='b', s=200)
plt.show()