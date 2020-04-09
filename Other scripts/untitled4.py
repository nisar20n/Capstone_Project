from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import scipy.signal
import scipy.fftpack
import numpy as np
import matplotlib.pyplot as plt
from scipy import pi
from scipy import signal
from scipy.fftpack import fft

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#
## Grab some test data.
#X, Y, Z = axes3d.get_test_data(0.05)
#
## Plot a basic wireframe.
#ax.plot_wireframe(Rx, Ry, Rz, rstride=10, cstride=10)
#
#plt.show()
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
t = np.arange(x) /1000

#def f(x, y):
#    return np.sin(np.sqrt(x ** 2 + y ** 2))
#
#x = np.linspace(-6, 6, 30)
#y = np.linspace(-6, 6, 30)
#
#X, Y = np.meshgrid(Rx, Ry)
#Z = f(X, Y)
#X,Y,Z=[1,2,3,4,5,6],[10,10,10,10,10,10],[10,10,10,10,10,10]
sos = signal.butter(10, 1, 'lp', fs=1000, output='sos')
filtered = signal.sosfilt(sos, Rx)

sos = signal.butter(10, 1, 'lp', fs=1000, output='sos')
filtered1 = signal.sosfilt(sos, Ry)

sos = signal.butter(10, 1, 'lp', fs=1000, output='sos')
filtered2 = signal.sosfilt(sos, Rz)
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.contour3D(X, Y, Z, 50, cmap='binary')


fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.plot(filtered, filtered1, filtered2)
ax.plot(t, filtered, filtered1)

ax.set_title('wireframe')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()