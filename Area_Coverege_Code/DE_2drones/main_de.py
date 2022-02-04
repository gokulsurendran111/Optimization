import numpy as np
import matplotlib.pyplot as plt
from radius_calc_final import *
import time

#def costfunc(x):
#
#    x1 = x[0]
#    x2 = x[1]
#
#    return x1**2 + x2**2
##    return 100*(x1**2 - x2)**2 + (1-x1)**2
#  # return (x1-2)^2*(x1+2)^2 + (x2-2)^2
#    # return -20*exp(-0.2*sqrt(0.5(x1^2+x2^2))) - exp(0.5(cos(2*pi*x1)+cos(2*pi*x2))) + exp(1) + 20

def initial_population(minim,maxim,NP,nvar):

    pop = np.zeros((NP,nvar))

    for i in range(nvar):
      pop[:,i] = np.random.uniform(low=minim[i], high=maxim[i], size=NP)

    return pop

def mutation(pop,NP,F):

    mut = 1

    while mut == 1:
        e1 = np.random.randint(NP)
        e2 = np.random.randint(NP)
        while e1 == e2:
            e2 = np.random.randint(NP)
    
        e3 = np.random.randint(NP)
        while e1 == e3 or e2 == e3:
            e3 = np.random.randint(NP)
 
        a = pop[e1,:]
        b = pop[e2,:]
        c = pop[e3,:]
    
        donor = a.copy()
 
        for i in range(len(donor)):
            donor[i] = a[i] + F*(b[i] - c[i])
 
        mut = mut_stop(donor)
   
    return donor

def mut_stop(donor):
    global minim, maxim, nvar

    ret = 0

    for i in range(nvar):
        if ((minim[i] < donor[i]) and (donor[i] < maxim[i])):
            ret = 0
        else:
            ret = 1
            return ret
    return ret

def recombination(xi,donor, Cp):

    trialvec = xi.copy()

    for i in range(len(xi)):
        crosscheck = np.random.uniform(low=0,high=1)

        if crosscheck < Cp:
            trialvec[i] = donor[i]
        else:
            trialvec[i] = xi[i]

    return trialvec

def selection(xi, trialvec):

    costxi = costfunc(xi)
    costtrial = costfunc(trialvec)

    if costxi < costtrial:
        return xi, costxi
    else:
        return trialvec, costtrial

def plot_area(X):
    
    X = best
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
    
    
    figure, axes = plt.subplots(1,1)
    
    plt.plot([0,0],[0,1000],"k",linewidth=5)
    plt.plot([0,1000],[0,0],"k",linewidth=5)
    plt.plot([0,1000],[1000,1000],"k",linewidth=5)
    plt.plot([1000,1000],[0,1000],"k",linewidth=5)
    
    for i in range(Ndrones):
        plt.scatter(Dloc[i,0], Dloc[i,1], marker='s', color='b')
        c_filled = plt.Circle((Dloc[i,0], Dloc[i,1]), R[i], fill=True, alpha = 0.2)
        c_boundary = plt.Circle((Dloc[i,0], Dloc[i,1]), R[i], fill=False)
        axes.add_artist( c_filled )
        axes.add_artist( c_boundary )
    
    plt.xlim([-200,1200])
    plt.ylim([-200,1200])
    axes.set_aspect(1)
    plt.pause(0.001)
    plt.show()

NP = 30
nvar = 6
minim = [0.0,0.0,100.0,  0.0,0.0,100.0]
maxim = [1000.0,1000.0,500.0,  1000.0,1000.0,500.0]
tol = 1e-6
F = 0.9
CP = 0.9
MAXGEN = 50

costval = 1000
pop = initial_population(minim,maxim,NP,nvar)
best = pop[0]
terminate = 0
genID = 0

gen_hist = []
bestcost_hist = []

print(pop)

while genID < MAXGEN and costval > tol and terminate == 0:
#    global pop, minim, maxim, NP, best, terminate, genID, costval
    
    start = time.time()
    newpop = pop.copy()

    costall = []

    for i in range(NP):
        xi = pop[i,:]
        
        donor = mutation(pop,NP,F)
        trialvec = recombination(xi, donor, CP)        
        nextgen, cost = selection(xi, trialvec)
        if cost < tol:
            costval = cost
            best = nextgen
            terminate = 1

        newpop[i,:] = nextgen
        costall.append(cost)
        print("Vector ",i," Evaluated")
 
    resall = np.zeros((NP,nvar+1))
    for i in range(NP):
        resall[i,0] = costall[i]
        resall[i,1:] = newpop[i]

    np.savetxt('Gen'+str(genID)+'.txt', resall)
    costval = min(costall)
    index_min = costall.index(costval)
    best = newpop[index_min]
    end = time.time()
    print("Gen completed ", genID, "  Best Cost : ", costval, "Time Taken : ", end-start)
#    plot_area(best)

    gen_hist.append(genID)
    bestcost_hist.append(costval)
    
    pop = newpop
    genID = genID + 1

print("Best : ",best)

    ### Plotting Area
    
     