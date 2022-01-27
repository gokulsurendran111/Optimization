import numpy as np
import matplotlib.pyplot as plt

terrain=np.loadtxt("zData.txt",dtype='float')

#user[0,0] gives x position of user 1
user=np.loadtxt("population.txt",dtype='float')

drone=np.array([[100,100,terrain[100,100]+50],[300,300,terrain[300,300]+50],[500,500,terrain[500,500]+50],
                [300,700,terrain[300,700]+50],[100,900,terrain[100,900]+50],[700,300,terrain[700,300]+50],
                [700,700,terrain[700,700]+50],[900,100,terrain[900,100]+50],[900,900,terrain[900,900]+50]])

plt.plot(user[:,0],user[:,1],'ro',drone[:,0],drone[:,1],'bx')

