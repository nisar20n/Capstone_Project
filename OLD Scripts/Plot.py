import time
import numpy as np
import matplotlib.pyplot as plt
import decimal
import csv
from scipy import pi
from scipy.fftpack import fft
import pandas as pd
import numpy as np

#def generate_text_file(length=1e6, ncols=20):
#    data = np.random.random((length, ncols))
#    np.savetxt('Data.txt', data, delimiter=',')
#
#def iter_loadtxt(filename, delimiter=',', skiprows=0, dtype=float):
#    def iter_func():
#        with open(filename, 'r') as infile:
#            for _ in range(skiprows):
#                next(infile)
#            for line in infile:
#                line = line.rstrip().split(delimiter)
#                for item in line:
#                    yield dtype(item)
#        iter_loadtxt.rowlength = len(line)
#
#    data = np.fromiter(iter_func(), dtype=dtype)
#    data = data.reshape((-1, iter_loadtxt.rowlength))
#    return data
#
##generate_text_file()
#data = iter_loadtxt('Data.txt')
#chunksize = 10 ** 8
#for chunk in pd.read_csv('Data.txt', chunksize=chunksize):
#    process(chunk)
#reader = csv.reader(open('Data.txt'))
#f = open("Data 3.txt", "r")
#g = open("datafile_fixed.txt", "w")
#
#for line in f:
#    if line.strip():
#        g.write("\t".join(line.split()[0:6]) + "\n")
#
#f.close()
#g.close()
data=np.genfromtxt('Data_5_Moving.txt',delimiter=',')
#A=data[0:,0]
#B=data[0:,1]
#C=data[0:,2]
#Rx=A
#Ry=B
#Rz=C
#D=data[0:,3]
#E=data[0:,4]
#F=data[0:,5]
#
#Gx=D
#Gy=E
#Gz=F
#G=data[0:,8]
#H=data[0:,9]
#I=data[0:,10]
#J=data[0:,11]
#K=data[0:,12]
#L=data[0:,13]
#M=data[0:,14]

Rx=data[0:,0]
Ry=data[0:,1]
Rz=data[0:,2]
Gx=data[0:,0]
Gy=data[0:,1]
Gz=data[0:,2]
#
##
##avg1=np.mean(Rx,0)
###avg2=np.mean(Ry,0)
###avg3=np.mean(Rz,0)
##
x=len(Rx)
t = np.arange(x) /1000
#
#
#for i in range(x):
#    value= (int(A[i])<<8)|int(B[i])
#    value1=(int(C[i])<<8)|int(D[i])
#    value2=(int(E[i])<<8)|int(F[i])
#    
#    value3= (int(G[i])<<8)|int(H[i])
#    value4=(int(I[i])<<8)|int(J[i])
##    value5=(int(K[i])<<8)|int(L[i])
##    
#    if(value1>32768):
#        value1=value1-65536
#    if(value>32768):
#        value=value-65536
#    if(value2>32768):
#        value2=value2-65536
#    if(value3>32768):
#        value3=value3-65536
#    if(value4>32768):
#        value4=value4-65536
##    if(value5>32768):
##        value5=value5-65536
#    Rx[i]=value/4096
#    Ry[i]=value1/4096
#    Rz[i]=value2/4096
#    Gx[i]=value3/131.2
#    Gy[i]=value4/131.2
##    Gz[i]=value5/131.2
##    if int(M[i])==0:
##        Rx[i]=value/16384
##        Ry[i]=value1/16384
##        Rz[i]=value2/16384
##        Gx[i]=value3/131.2
##        Gy[i]=value4/131.2
##        Gz[i]=value5/131.2
##        print("0")
##    if int(M[i])==1:
##        Rx[i]=value/8192
##        Ry[i]=value1/8192
##        Rz[i]=value2/8192
##        Gx[i]=value3/131.2
##        Gy[i]=value4/131.2
##        Gz[i]=value5/131.2
##        print("1")
##    if int(M[i])==2:
##        Rx[i]=value/4096
##        Ry[i]=value1/4096
##        Rz[i]=value2/4096
##        Gx[i]=value3/131.2
##        Gy[i]=value4/131.2
##        Gz[i]=value5/131.2
##        print("2")
##    if int(M[i])==3:
##        Rx[i]=value/2048
##        Ry[i]=value1/2048
##        Rz[i]=value2/2048
##        Gx[i]=value3/131.2
##        Gy[i]=value4/131.2
##        Gz[i]=value5/131.2
##        print("3")
#        
Fx=np.square(Rx)       
Fy=np.square(Ry)
Fz=np.square(Rz)
Ft=Fx+Fy+Fz
Tx=np.sqrt(Ft)
#
plt.figure(1)
plt.plot(t,Tx,"b-*")

plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
plt.xlabel('time')
plt.ylabel('Total Force')

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


#plt.figure(7)
#plt.plot(t,Gz,"y-*")
#plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
#         linestyle='-',linewidth=2)
#plt.minorticks_on()
#plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
#         linestyle='-',linewidth=2)
#plt.xlabel('time')
#plt.ylabel('Gz')