import numpy as np
import math
import time

def pathloss(Drone_coord, r):
    dx = Drone_coord[0]
    dy = Drone_coord[1]
    dz = Drone_coord[2]
    
    Delta_h = dz
    hor_dist = r
    dist = np.sqrt( Delta_h**2 + hor_dist**2 )
    
    theta = math.atan2(Delta_h , hor_dist)
    theta = np.rad2deg(theta)
    
#    a = 9.61 # Urban
#    b = 0.16
#    eta_LOS = 1.0
#    eta_NLOS = 20
    
    a = 12.08  # Dense Urban
    b = 0.11
    eta_LOS = 1.6
    eta_NLOS = 23    
    
    PLOS = 1.0/(1 + a*np.exp( -b*(theta - a) ))
    PNLOS = 1 - PLOS
    
    fc = 2.0*10**9
    c = 299792458.0
    
    PL = 20*np.log10(4*np.pi*fc*dist/c) + PLOS*eta_LOS + PNLOS*eta_NLOS
    return PL

def calc_radius(D1, gamma, reg_limit):

    x_lim = min(D1[0], reg_limit[0] - D1[0])
    y_lim = min(D1[1], reg_limit[1] - D1[1])
    r_lim = min(x_lim, y_lim)
    
    r_arr = np.linspace(0,1000,500)
    
    f1 = []
    for r in r_arr:
        pl = pathloss(D1, r)
        if pl < gamma:
            u = 1
        else:
            u = 0
        f1.append(u)
    
    for i in range(len(f1)):
        if f1[i] == 1:
            k = i
            
    radius = r_arr[k]
    return radius

def point_in_coverage(xp, yp, Dloc, R):
    ret = 0
    
    for i in range(len(R)):
        dist = np.sqrt( (xp - Dloc[i,0])**2 + (yp - Dloc[i,1])**2 )
        if dist < R[i]:
            ret = 1
            break
    
    return ret 

def costfunc(X):
    reg_limit = [1000.0, 1000.0]
    gamma = 100
    
    Ndrones = 2
    
    Dloc = np.zeros((Ndrones,3))
    Dloc[0] = X[0:3]
    Dloc[1] = X[3:6]
#    Dloc[2] = X[6:9]
#    Dloc[3] = X[9:12]
#    Dloc[4] = X[12:15]
#    Dloc[5] = X[15:18]
    
    R = np.zeros(Ndrones)
    for k in range(Ndrones):
        R[k] = calc_radius(Dloc[k], gamma, reg_limit)
    
    NP_inside = 0
    NPMC = 50000
    xp_mc = []
    yp_mc = []
    for inp in range(NPMC):
        xp = np.random.uniform(0,reg_limit[0])
        yp = np.random.uniform(0,reg_limit[1])
        if (point_in_coverage(xp,yp,Dloc,R) == 1):
            NP_inside = NP_inside + 1
            xp_mc.append(xp)
            yp_mc.append(yp)

    Jvalue = 1-NP_inside/NPMC 
#    print(Jvalue)
    return Jvalue
