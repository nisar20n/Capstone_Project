import time
import numpy as np
import matplotlib.pyplot as plt
import decimal
import csv
from scipy import pi
from scipy.fftpack import fft


data=np.genfromtxt('Data_4_Stationary.txt',delimiter=',')
Rx=data[0:,0]
Ry=data[0:,1]
Rz=data[0:,2]
Gx=data[0:,3]
Gy=data[0:,4]
Gz=data[0:,5]



avg1=np.mean(Rx,0)
#avg2=np.mean(Ry,0)
#avg3=np.mean(Rz,0)

x=len(Rx)
t = np.arange(x) /80



        


plt.figure(2)
plt.plot(t,Rx,"b-*")

plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rx')

plt.figure(3)
plt.plot(t,Ry,"r-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Ry')

plt.figure(4)
plt.plot(t,Rz,"g-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Rz')

plt.figure(5)
plt.plot(t,Gx,"m-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Gx')


plt.figure(6)
plt.plot(t,Gy,"k-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Gy')


plt.figure(7)
plt.plot(t,Gz,"y-*")
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Gz')