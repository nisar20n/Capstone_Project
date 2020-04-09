# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:20:46 2020

@author: Nazibul
"""

import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import decimal
import csv
from scipy import pi
from scipy.fftpack import fft

g =np.arange(10)
o =np.arange(10)
h = [9,10,11,12]

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

x=len(Rx)
t = np.arange(x)/1024

plt.figure(1)
ax=plt.axes(xlim=(0,max(t)),ylim=(min(Rx),max(Rx)))
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rx')

plt.figure(2)
ax1=plt.axes(xlim=(0,max(t)),ylim=(min(Rz),max(Rz)))
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Ry')
#
[line]=ax.plot([],[],lw=2)

[line1]=ax1.plot([],[],lw=2)

#    
def init():
    line.set_data([],[])
#    plt.savefig('figurea0.png')
#    plt.pause(sec)
    return([line])
    
def animate(i):
    line.set_data(t[:i],Rx[:i])
    
#    filename='figurea'+str(i)+'.png'
#    plt.savefig(filename)
#    plt.pause(sec)
    return([line])
    
def init1():
    line1.set_data([],[])
#    plt.savefig('figurea0.png')
#    plt.pause(sec)
    return([line1])
    
def animate1(i):
    line1.set_data(t[:i],Rz[:i])
    
#    filename='figurea'+str(i)+'.png'
#    plt.savefig(filename)
#    plt.pause(sec)
    return([line1])
    


animation=anim.FuncAnimation(plt.figure(1),animate,init_func=init,frames=len(Rx),interval=1,
                             blit=True)

animation1=anim.FuncAnimation(plt.figure(2),animate1,init_func=init1,frames=len(Rx),interval=1,
                             blit=True)
#
#init()
#frame=np.arange(len(Rz)+1)
#for f in frame:
#    animate(f)