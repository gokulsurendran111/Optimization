import numpy as np

def cost(x):

    x1 = x[0]
    x2 = x[1]

    # return x1^2 + x2^2
    return 100*(x1^2 - x2)^2 + (1-x1)^2
  # return (x1-2)^2*(x1+2)^2 + (x2-2)^2
    # return -20*exp(-0.2*sqrt(0.5(x1^2+x2^2))) - exp(0.5(cos(2*pi*x1)+cos(2*pi*x2))) + exp(1) + 20

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
 
        donor = a
 
        for i in range(len(donor)):
            donor[i] = a[i] + F*(b[i] - c[i])
 
        mut = mut_stop(donor)
   
    return donor

def mut_stop(donor):
    global minim, maxim, nvar

    ret = 0

    for i in range(nvar):
        if (minim[i] < donor[i] and donor[i] < maxim[i]):
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

    costxi = cost(xi)
    costtrial = cost(trialvec)

    if costxi < costtrial:
        return xi, costxi
    else:
        return trialvec, costtrial

