# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 02:26:38 2020

@author: Nazibul
"""

import time
import math
import numpy as np
import matplotlib.pyplot as plt
import decimal
import csv
from scipy import pi
from scipy.fftpack import fft




hpf=0.02
lpf=.98
dt=1/1000
data=np.genfromtxt('angle_test2.txt',delimiter=',')
Rx=data[1:,0]
Ry=data[1:,1]
Rz=data[1:,2]
Gx=data[1:,3]
Gy=data[1:,4]
Gz=data[1:,5]
x=len(Rx)
t = np.arange(x) /80

thetaccX = lpf*np.arctan2(Rz,Ry)* 180 / np.pi
thetaccY = lpf*np.arctan2(Rx,Rz)* 180 / np.pi
thetaccZ = lpf*np.arctan2(Ry,Rx)* 180 / np.pi

thetaX = np.zeros(len(Gx))
thetaY =  np.zeros(len(Gx))
thetaZ =  np.zeros(len(Gx))
for i in range(0,len(Gx)):    
    if i==0:
        thetaX[i] = (hpf*thetaX[i]*dt)+thetaccX[i]
        thetaY[i] = (hpf*thetaY[i]*dt)+thetaccY[i]
        thetaZ[i] = (hpf*thetaZ[i]*dt)+thetaccZ[i]
    else:
        thetaX[i] = (hpf*(thetaX[i-1]+Gx[i]*dt))+thetaccX[i]
        thetaY[i] = (hpf*(thetaY[i-1]+Gy[i]*dt))+thetaccY[i]
        thetaZ[i] = (hpf*(thetaZ[i-1]+Gz[i]*dt))+thetaccZ[i]




plt.figure(8)
plt.plot(thetaX,"b-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rx')        


plt.figure(9)
plt.plot(thetaY,"b-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Ry')        

plt.figure(10)
plt.plot(thetaZ,"b-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rz')  

#la=5
#ka=8
#m = np.array([-1, +1, +1, -1])
#n = np.array([-1, -1, +1, +1])
#k=np.arctan2(Rx,Ry)
#ca=math.atan2(la,ka)
#y = np.linspace(-10, 10)
#plt.plot(y, np.arctan(y))
#plt.axis('tight')
#plt.show()


