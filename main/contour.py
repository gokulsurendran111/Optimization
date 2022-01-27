import matplotlib.pyplot as plt
import numpy as np
  
# feature_x = np.linspace(-5.0, 3.0, 70)
# feature_y = np.linspace(-5.0, 3.0, 70)

from constraints import *
from terrain_popu import *
from main import cost



x1 = range(0,1001,100)
# check = np.zeros([11,11])
check=[]
for x in x1:
    DroneLoc[2,0] = x
    # costvalue = np.zeros(11)
    costvalue=[]
    for y in x1:
        DroneLoc[2,1] = y
        costvalue.append(cost(UserLoc, DroneLoc))
    check.append(costvalue)
                
        
        
        # print(DroneLoc[0])
        # np.insert(costvalue,y,cost(UserLoc, DroneLoc))
        # np.insert(check,x,costvalue,0)
                
  
# Creating 2-D grid of features
lenx1=len(x1)
[X, Y] = np.meshgrid(lenx1,lenx1)
  
fig, ax = plt.subplots(1, 1)
# surf = ax.plot_surface(check)
# Z = X ** 2 + Y ** 2

# npche=np.array(check) 
# plots filled contour plot
ax.contourf(check)
  
ax.set_title('Filled Contour Plot')
ax.set_xlabel('feature_x')
ax.set_ylabel('feature_y')
  
# plt.show()
