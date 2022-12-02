# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Change this to the directory where you store KITTI data

Odo_Dir = 'KITTI_SAMPLE/ODOMETRY'
RAW_Dir = 'KITTI_SAMPLE/RAW'
date = '2011_09_26'
drive = '0009'

# Specify the dataset to load
sequence = '04'
import pykitti

# Load the data
data = pykitti.raw(RAW_Dir, date, drive, frames=range(0, 50, 1))

#load the image from the Pykitti database
import numpy as np
image = np.array(data.get_cam2(0), dtype='uint8')

#read the velo information from the dataset
velo = data.get_velo(0)
print(velo)

print(np.shape(velo)) #(122320, 4) we have 4*4 velo informations
# remove depth inferior to 5 (by the first element 'x values')
velo_data_clipped = velo[velo[:,0]>5]
print(velo_data_clipped)
print(np.shape(velo_data_clipped))#(27608, 4)

# extract projection matrix from Lidar to camera
calcam = data.calib.T_cam2_velo #T"
print(calcam)
print(len(calcam))# 4

# extract K matrix of camera 2
K = np.array(data.calib.K_cam2) # Camera intrinsic parameter K

#Make K matrix the same dimension as T"
K= np.hstack((K,np.zeros((K.shape[0],1))))
c = [0,0,0,1]
K = np.vstack([K,c])
print(K)

#T = K @ T"
T = K@calcam
print(T)

#Do the Projection
P = T@velo_data_clipped.T
print(P)
P_2D = P[:2]/P[2, :]
print(P_2D)
imgw , imgh = image.shape[:2]

# filter point out of the image
u,v= P_2D
u_out = np.logical_or(u<0, u>imgw)
v_out = np.logical_or(v<0, v>imgh)
outlier = np.logical_or(u_out, v_out)
P_2D = np.delete(P_2D,np.where(outlier),axis=1)

# generate color map from depth
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)
plt.axis([0,imgh,imgw,0])
plt.imshow(image)
plt.scatter([u],[v],c=1/P[2],cmap='jet',alpha=0.5,s=10)
plt.savefig(f'result/plot.png',bbox_inches='tight')
plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
