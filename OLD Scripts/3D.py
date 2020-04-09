# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 05:52:45 2020

@author: Nazibul
"""

import numpy as np
import matplotlib.pyplot as plt
import decimal
import csv
from scipy import pi
from scipy.fftpack import fft
from mpl_toolkits.mplot3d import axes3d

data=np.genfromtxt('Data_4_Stationary.txt',delimiter=',')
Rx=data[1:,0]
Ry=data[1:,1]
Rz=data[1:,2]

Gx=data[1:,3]
Gy=data[1:,4]
Gz=data[1:,5]
avg1=np.mean(Rx,0)
avg2=np.mean(Ry,0)
avg3=np.mean(Rz,0)

X,Y,Z=[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]
x=len(Rx)
t = np.arange(x) /1000
K=np.array(Z)
L=np.array(X)
M=np.array(Y)
fig=plt.figure()
#ax=fig.add_subplot(111, projection='3d')
ax = fig.gca(projection='3d')
surf = ax.plot_trisurf(Rx, Ry, Rz, linewidth=0, antialiased=False)
plt . show ( )
#ax.plot_wireframe(X,Y,K)
#
#plt.show()