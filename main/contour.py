import matplotlib.pyplot as plt
import numpy as np
  
# feature_x = np.linspace(-5.0, 3.0, 70)
# feature_y = np.linspace(-5.0, 3.0, 70)

from constraints import *
from terrain_popu import *
from main import cost

# np.random.seed()



x1 = range(0,1001,50)
# check = np.zeros([11,11])
check=[]
for x in x1:
    DroneLoc[5,0] = x
    # costvalue = np.zeros(11)
    costvalue=[]
    for y in x1:
        DroneLoc[5,1] = y
        costvalue.append(cost(UserLoc, DroneLoc))
    check.append(costvalue)
                
        
        
        # print(DroneLoc[0])
        # np.insert(costvalue,y,cost(UserLoc, DroneLoc))
        # np.insert(check,x,costvalue,0)
x1=np.array(x1)               
check=np.array(check)  
# Creating 2-D grid of features
lenx1=len(x1)
[X, Y] = np.meshgrid(lenx1,lenx1)
  
fig, ax = plt.subplots(1, 1)
# fig,ax2=plt.subplots(1,1)
# surf = ax.plot_surface(check)
# Z = X ** 2 + Y ** 2

# npche=np.array(check) 
# plots filled contour plot
cp=ax.contourf(x1,x1.copy().T,check)
fig.colorbar(cp)
# cp1=ax2.contour(x1,x1.copy().T,check)
 
ax.set_title('Objective space by varying two variables')
ax.set_xlabel('x6')
ax.set_ylabel('y6')
  
plt.show()



# Import libraries
# from mpl_toolkits import mplot3d


 
 
# Creating dataset
# x = np.array(x1)
# y = x.copy().T # transpose
# z = check
 
# # Creating figure
# fig = plt.figure(figsize =(14, 9))
# ax = plt.axes(projection ='3d')
 
# # Creating plot
# ax.plot_surface(x, y, z)
 
# # show plot
# plt.show()
