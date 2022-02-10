import numpy as np
from init_terrain_popu_drones import *
from radius_calc_final import *
from cost_calculation import *

def report_card(best):
    global Ndrones, Nusers
    
    X = best
    reg_limit = [1000.0, 1000.0]
    
    Dloc = np.zeros((Ndrones,3))
    Dloc[0] = X[0:3]
    Dloc[1] = X[3:6]
    Dloc[2] = X[6:9]
    Dloc[3] = X[9:12]
    Dloc[4] = X[12:15]
    Dloc[5] = X[15:18]    
    
    ## Terrain Plot
    fig = plt.figure(figsize=(12,6))
    ax = fig.add_subplot(1,2,1,projection ="3d")
    ax.set_zlim([0,500])
    
    ax.plot_wireframe(terrain_x, terrain_y, terrain_z, color='k', linewidth=0.2)
    
    ax.set_xlabel("Horizontal X axis (m)")
    ax.set_ylabel("Horizontal Y axis (m)")
    ax.set_zlabel("Altitude (m)")
    ax.scatter3D(UserLoc[:,0], UserLoc[:,1], UserLoc[:,2], marker='o', color='r', s=20)
    ax.scatter3D(Dloc[:,0], Dloc[:,1], Dloc[:,2], marker='s', color='b', s=50)
    
    ax2 = fig.add_subplot(1,2,2)
    
    R = np.zeros(Ndrones)
    for k in range(Ndrones):
        R[k] = calc_radius(Dloc[k], gamma, reg_limit)
       
    plt.plot([0,0],[0,1000],"k",linewidth=5)
    plt.plot([0,1000],[0,0],"k",linewidth=5)
    plt.plot([0,1000],[1000,1000],"k",linewidth=5)
    plt.plot([1000,1000],[0,1000],"k",linewidth=5)
    
    for i in range(Ndrones):
        plt.scatter(Dloc[i,0], Dloc[i,1], marker='s', color='b')
        plt.text(Dloc[i,0], Dloc[i,1], str(i), color='r', fontsize=10)
        c_filled = plt.Circle((Dloc[i,0], Dloc[i,1]), R[i], fill=True, alpha = 0.2)
        c_boundary = plt.Circle((Dloc[i,0], Dloc[i,1]), R[i], fill=False)
        ax2.add_artist( c_filled )
        ax2.add_artist( c_boundary )
    
    plt.xlim([-200,1200])
    plt.ylim([-200,1200])
    ax2.set_aspect(1)

    J, UCS = costfunc(best, 1)
    plt.scatter(UserLoc[:,0], UserLoc[:,1], marker='o', color='r', s=20)
    
    Nconnected = 0
    for i in range(Nusers):
        plt.text(UserLoc[i,0], UserLoc[i,1], str(i), color="black", fontsize=8)
        if (sum(UCS[i,:]) > 0):
            Nconnected += 1
            plt.scatter(UserLoc[i,0], UserLoc[i,1], marker='o', color='g', s=20)

    plt.show()
    
    for i in range(Ndrones):
        print("Users Connected to Drone ", str(i), " : ", str(sum(UCS[:,i])), "\n")
    
    print("Total Numbers of Users Connected : ", Nconnected)