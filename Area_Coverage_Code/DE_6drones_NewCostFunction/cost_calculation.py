import numpy as np
from radius_calc_final import *
from constraints import *
from terrain_popu import *

def costfunc(Dloc_Array, retUCS=0):
    global UserLoc, User_Weights, gamma
    
    reg_limit = [1000.0, 1000.0]
    gamma = 100
    Rmax = 500
    
    Ndrones = 6
    Nusers = len(UserLoc)
    
    Dloc = np.zeros((Ndrones,3))
    Dloc[0] = Dloc_Array[0:3]
    Dloc[1] = Dloc_Array[3:6]
    Dloc[2] = Dloc_Array[6:9]
    Dloc[3] = Dloc_Array[9:12]
    Dloc[4] = Dloc_Array[12:15]
    Dloc[5] = Dloc_Array[15:18]
    
    ## Area Coverage Calculation ##############################################
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

    Area_not_covered = 1-NP_inside/NPMC 
    
    ## Pathloss Calculation ###################################################
    User_Connection_status = np.zeros((Nusers,Ndrones))
    wtPlij_sum = 0
    for i in range(Ndrones):
        for j in range(Nusers):
            Plij = pathloss_user_drone(Dloc[i], UserLoc[j])
            distij = DroneUser_Distance(Dloc[i], UserLoc[j])
#            print(" ")
#            print("User ",j, " Drone ",i)
#            print("Path Loss ", Plij)
#            print("Distance ", distij)
            if (Plij <= gamma and distij <= Rmax and sum(User_Connection_status[:,i]) < 10):
                User_Connection_status[j,i] = 1
#                print("User ",j, " connected to Drone ",i)
                wtPlij = Plij/User_Weights[j]
                wtPlij_sum += wtPlij
            elif (Plij > gamma or distij > Rmax):
                wtPlij_sum += gamma
    
#    print("User Connection Status = \n", User_Connection_status)
    wtPlij_sum = wtPlij_sum/(gamma*Nusers)
#    print("Sum PLij/w = ", wtPlij_sum)

    ## Drone Distance Penalty Calculation #####################################
    
    DroneDistSum = 0
    Ncomb = 1
    for i in range(Ndrones):
        for j in range(Ndrones):
            dist_didj = DroneDistance(Dloc[i], Dloc[j])
            if (dist_didj <= Rmax):
                DroneDistSum += 0.0
            else:
                Ncomb += 1
                DroneDistSum += dist_didj
                
#    print("Drone Dist Sum = ")
    DDS = DroneDistSum/(1000*Ncomb)
#    print(DDS)
    
    ## Number of Users connected
    NusersConnected = 0
    for i in range(50):
        if (sum(User_Connection_status[i,:]) >= 1):
            NusersConnected += 1

    Jvalue = Area_not_covered + wtPlij_sum + DDS + NusersConnected/50
    
    if retUCS == 1:
        return Jvalue, User_Connection_status
    else:
        return Jvalue

"""
Dloc_Array = [230.92224307, 694.27668201, 463.84361279, 901.98836072,
       636.57325282, 441.88016907, 827.39543398, 950.89409247,
       226.3154561 , 291.47786536, 138.22019431, 449.52405805,
       735.51572784, 777.51932795, 479.4189237 , 986.23842011,
       238.21483864, 477.31988406]

COST, UCS = costfunc(Dloc_Array)
print("Total Cost Value = ")
print(COST)

plot_area(Dloc_Array)

plt.scatter(UserLoc[:,0], UserLoc[:,1], marker='o', color='r', s=20)

for i in range(50):
    plt.text(UserLoc[i,0], UserLoc[i,1], str(i), color="black", fontsize=8)
    if (sum(UCS[i,:]) > 0):
        plt.scatter(UserLoc[i,0], UserLoc[i,1], marker='o', color='g', s=20)

"""

