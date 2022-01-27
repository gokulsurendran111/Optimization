import math
import numpy as np

def pathloss(Drone_coord, User_coord):
    dx = Drone_coord[0]
    dy = Drone_coord[1]
    dz = Drone_coord[2]
    
    ux = User_coord[0]
    uy = User_coord[1]
    uz = User_coord[2]
    
    Delta_h = dz - uz
    hor_dist = np.sqrt( (dx-ux)**2 + (dy-uy)**2 )
    dist = np.sqrt( (dx-ux)**2 + (dy-uy)**2 + (dz-uz)**2 )
    
    theta = math.atan(Delta_h / hor_dist)
    theta = np.rad2deg(theta)
    
    a = 9.61
    b = 0.16
    eta_LOS = 1.0
    eta_NLOS = 20
    
    PLOS = 1.0/(1 + a*np.exp( -b*(theta - a) ))
    PNLOS = 1 - PLOS
    
    fc = 2.0*10**9
    c = 299792458.0
    
    PL = 20*np.log(4*np.pi*fc*dist/c) + PLOS*eta_LOS + PNLOS*eta_NLOS
    return PL

def DroneDistance(Drone1_coord, Drone2_coord):
    d1x = Drone1_coord[0]
    d1y = Drone1_coord[1]
    d1z = Drone1_coord[2]

    d2x = Drone2_coord[0]
    d2y = Drone2_coord[1]
    d2z = Drone2_coord[2]    

    dist = np.sqrt( (d1x-d2x)**2 + (d1y-d2y)**2 + (d1z-d2z)**2 )

    return dist

def DroneUser_Distance(Drone_coord, User_coord):
    dx = Drone_coord[0]
    dy = Drone_coord[1]
    dz = Drone_coord[2]
    
    ux = User_coord[0]
    uy = User_coord[1]
    uz = User_coord[2]

    dist = np.sqrt( (dx-ux)**2 + (dy-uy)**2 + (dz-uz)**2 )

    return dist














