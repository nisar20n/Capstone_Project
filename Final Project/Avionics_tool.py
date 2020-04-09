
import tkinter as tk
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import decimal
import csv
from scipy import pi
from tkinter import *
from scipy.fftpack import fft
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import tkinter
import numpy as np
from scipy import signal
import scipy.fftpack
from tkinter import messagebox
import matplotlib.animation as anim
from PIL import ImageTk, Image

def save():
    
    def save_data():
        lolo=entry.get()
        file_name=lolo+".txt"
        np.savetxt(file_name, np.column_stack([filtered,filtered1,filtered2,gfiltered,gfiltered1,gfiltered2,thetaX,thetaY,thetaZ]))
        root9.destroy()
    def on_closing():
        global dhaka
        
        dhaka='normal'
        root9.destroy()
    global dhaka
    if dhaka=='abnormal':
        root9 = Toplevel(root)
        dhaka=root9.state()  
        root9.protocol("WM_DELETE_WINDOW", on_closing)
        geo=root9.geometry
        geo("300x100+400+400")
        label1=tk.Label(root9,justify=tk.LEFT,
              padx = 10, text="Name your text File")
        entry=Entry(root9)
        entry.grid(row=0,column=1)
        btn=Button(root9,text="Save",bg="purple",fg="white",command=save_data)
        btn.grid(row=2,columnspan=2)
        label1.grid(row=0)
        root9['bg'] = 'tomato2'
        root9.wm_title("Save Filtered Data")
        root9.mainloop() 
    
    



def Data_Comparison():
    class MyClass:
        def __init__(self, frame):
            self.va = StringVar(root6, "0") 
            self.valuese = {"X-Axis Acceleraion" : "1", "Y-Axis Acceleraion" : "2", "Z-Axis Acceleraion" : "3", "X-Axis Gyroscope" : "4",  "Y-Axis Gyroscope" : "5", 
                            "Z-Axis Gyroscope" : "6","Total Force" : "7"} 
            self.frame = frame
            
            self.fig = Figure(figsize=(12, 6), dpi=100)
            self.ax = self.fig.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
            toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
            toolbar.update()
            self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
                            
            def ShowC():
                global poil
                poi =int(self.va.get())
               
                if poi==1:
                    self.plot_graph()
                if poi==2:
                    self.plot_graph1()
                if poi==3:
                    self.plot_graph2()
                if poi==4:
                    self.plot_graph3()
                if poi==5:
                    self.plot_graph4()
                if poi==6:
                    self.plot_graph5()
                if poi==7:
                    self.plot_graph6()
            for (text, value) in self.valuese.items(): 
                Radiobutton(root6, text = text, variable = self.va, command=ShowC,value = value, indicator = 0, background = "light blue").pack(side=tk.LEFT,before=toolbar,anchor=N)
                            
                            
        def plot_graph(self):
            self.ax.cla()
            self.ax.plot(t,Rx,"r-*",label='Unfiltered Data')
            self.ax.plot(t,filtered,"g-*",label='Filtered Data')
            self.ax.legend(loc="upper right")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('X-Axis Acceleraion (g)')
            self.ax.set_title('X-Axis Accelerometer Filtered vs Unfiltered Data')
            self.canvas.draw()
        def plot_graph1(self):
            self.ax.cla()
            self.ax.plot(t,Ry,"r-*",label='Unfiltered Data')
            self.ax.plot(t,filtered1,"g-*",label='Filtered Data')
            self.ax.legend(loc="upper right")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Y-Axis Acceleraion (g)')
            self.ax.set_title('Y-Axis Accelerometer Filtered vs Unfiltered Data')
            self.canvas.draw()
        def plot_graph2(self):
            self.ax.cla()
            self.ax.plot(t,Rz,"r-*",label='Unfiltered Data')
            self.ax.plot(t,filtered2,"g-*",label='Filtered Data')
            self.ax.legend(loc="upper right")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Z-Axis Acceleraion (g)')
            self.ax.set_title('Z-Axis Accelerometer Filtered vs Unfiltered Data')
            self.canvas.draw()
        def plot_graph3(self):
            self.ax.cla()
            self.ax.plot(t,Gx,"r-*",label='Unfiltered Data')
            self.ax.plot(t,gfiltered,"g-*",label='Filtered Data')
            self.ax.legend(loc="upper right")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('X-Axis Angular Velocity (deg/s)')
            self.ax.set_title('X-Axis Gyroscope Filtered vs Unfiltered Data')
            self.canvas.draw()
        def plot_graph4(self):
            self.ax.cla()
            self.ax.plot(t,Gy,"r-*",label='Unfiltered Data')
            self.ax.plot(t,gfiltered1,"g-*",label='Filtered Data')
            self.ax.legend(loc="upper right")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Y-Axis Angular Velocity (deg/s)')
            self.ax.set_title('Y-Axis Gyroscope Filtered vs Unfiltered Data')
            self.canvas.draw()
        def plot_graph5(self):
            self.ax.cla()
            self.ax.plot(t,Gz,"r-*",label='Unfiltered Data')
            self.ax.plot(t,gfiltered2,"g-*",label='Filtered Data')
            self.ax.legend(loc="upper right")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Z-Axis Angular Velocity (deg/s)')
            self.ax.set_title('Z-Axis Gyroscope Filtered vs Unfiltered Data')
            self.canvas.draw()
        def plot_graph6(self):
            self.ax.cla()
            self.ax.plot(t,Tx,"r-*",label='Unfiltered Data')
            self.ax.plot(t,Px,"g-*",label='Filtered Data')
            self.ax.legend(loc="upper right")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Magnitude of total Acceleration(g)')
            self.ax.set_title('Total Acceleration Filtered vs Unfiltered')
            self.canvas.draw()
            
    def on_closing():
        global khuta
        
        khuta='abnormal'
        root6.destroy()
    global Px
    Qx=np.square(filtered)       
    Qy=np.square(filtered1)
    Qz=np.square(filtered2)
    Qt=Qx+Qy+Qz
    Px=np.sqrt(Qt)    
    global khuta
    if khuta=='abnormal':
        root6 = Toplevel(root)
        khuta=root6.state()  
        root6.protocol("WM_DELETE_WINDOW", on_closing)
        geo=root6.geometry
        geo("+300+0")
        root6['bg'] = 'orange'
        root6.wm_title("Data Comparison")
        MyFrame = tkinter.Frame(root6)
        MyClass(MyFrame)
        MyFrame.pack()
        root6.mainloop() 
    
def Filters1():
    class MyClass:
        def __init__(self, frame):
            self.vat = StringVar(root5, "0") 
            self.valuest = {"X-Axis Gyroscope" : "1", "Y-Axis Gyroscope" : "2", "Z-Axis Gyroscope" : "3", "X-Axis FFT" : "4",  "Y-Axis FFT" : "5", "Z-Axis FFT" : "6"} 
            self.frame = frame
            
            self.fig = Figure(figsize=(11, 6), dpi=100)
            self.ax = self.fig.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
            toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
            toolbar.update()
            self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
                            
            def ShowC():
                global poila
                poila =int(self.vat.get())
                
                if poila==1:
                    self.plot_graph()
                if poila==2:
                    self.plot_graph1()
                if poila==3:
                    self.plot_graph3()
                if poila==4:
                    self.plot_Gx()
                if poila==5:
                    self.plot_Gy()
                if poila==6:
                    self.plot_Gz()
            for (text, value) in self.valuest.items(): 
                Radiobutton(root5, text = text, variable = self.vat, command=ShowC,value = value, indicator = 0, background = "light blue").pack(side=tk.LEFT,before=toolbar,anchor=N)
                            
                            
        def plot_graph(self):
            self.ax.cla()
            self.ax.plot(t,gfiltered,"r-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('X-Axis Angular Velocity (deg/s)')
            self.ax.set_title('X-Axis Gyroscope Filtered Data')
            self.canvas.draw()
        def plot_graph1(self):
            self.ax.cla()
            self.ax.plot(t,gfiltered1,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Y-Axis Angular Velocity (deg/s)')
            self.ax.set_title('Y-Axis Accelerometer Filtered Data')
            self.canvas.draw()
        def plot_graph3(self):
            self.ax.cla()
            self.ax.plot(t,gfiltered2,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Z-Axis Angular Velocity (deg/s)')
            self.ax.set_title('Z-Axis Accelerometer Filtered Data')
            self.canvas.draw()
        def plot_Gx(self):
            self.ax.cla()
            self.ax.semilogy(frequency,fgx,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('X-Axis Gyroscope FFT Plot After Filtering')
            self.canvas.draw()
        def plot_Gy(self):
            self.ax.cla()
            self.ax.semilogy(frequency,fgy,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('Y-Axis Gyroscope FFT Plot After Filtering')
            self.canvas.draw()
        def plot_Gz(self):
            self.ax.cla()
            self.ax.semilogy(frequency,fgz,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('Z-Axis Gyroscope FFT Plot After Filtering')
            self.canvas.draw()
            
    def show_data():
        print("hello")
        global gpasa
        global ghaga
        global gsos
        global gfiltered
        global gfiltered1
        global gfiltered2
        global fgx,fgy,fgz
        

        txt.delete('0.0','end')
        gpasa=entry.get()
        ghaga=var.get()
        jiji=var1.get()
       
        if ghaga==1:
            ghaga='lp'
            melt="Low Pass Filter"
        else:
            ghaga='hp'
            melt="High Pass Filter"
    
        sentence="Hello,You have chosen a "+melt+" with a cut off frequency of "+gpasa+" Hz.";
        txt.insert(0.0,sentence);
        hello=int(gpasa)
        gsos = signal.butter(10,hello,ghaga, fs=fs, output='sos')
        if jiji==1:
            gfiltered =signal.sosfilt(gsos, Gx) 
        if jiji==2:
            gfiltered1 =signal.sosfilt(gsos, Gy) 
        if jiji==3:
            gfiltered2 =signal.sosfilt(gsos, Gz)    
       
        freqx_data = fft(gfiltered)
        lu=len(frequency)
        fgx = np.abs (freqx_data [0:lu])/q
        
        freqy_data = fft(gfiltered1)
        fgy = np.abs (freqy_data [0:lu])/q
        
        freqz_data = fft(gfiltered2)
        fgz = np.abs (freqz_data [0:lu])/q
    def on_closing():
        global nuta
        
        nuta='abnormal'
        root5.destroy()
        
    global nuta
    if nuta=='abnormal':
        root5 = Toplevel(root)
        nuta=root5.state()  
        root5.protocol("WM_DELETE_WINDOW", on_closing)
        geo=root5.geometry
        geo("+150+0")
        root5['bg'] = 'orange'
        root5.wm_title("Gyroscope Data Filtering")
        label1=tk.Label(root5,justify=tk.CENTER, text="Cut off Frequency:")
        label2=tk.Label(root5,justify=tk.CENTER, text="Filter Type:")
        label3=tk.Label(root5,justify=tk.CENTER, text="Select Axis to Apply Filter:")
        entry=Entry(root5)
        var=IntVar() 
        var1=IntVar() 
        rd1=Radiobutton(root5,text="Lp",variable=var,value=1)
        rd2=Radiobutton(root5,text="Hp",variable=var,value=2)
        rd3=Radiobutton(root5,text="X",variable=var1,value=1)
        rd4=Radiobutton(root5,text="Y",variable=var1,value=2)
        rd5=Radiobutton(root5,text="Z",variable=var1,value=3)
        label1.pack(side=tk.LEFT,anchor=N)
        entry.pack(side=tk.LEFT,anchor=N)
        label2.place(relx=0, x=45, y=22.5, anchor=N)
        label3.place(relx=0, x=75, y=52, anchor=N)
        rd1.place(relx=0, x=120, y=20, anchor=N)
        rd2.place(relx=0, x=200, y=20, anchor=N)
        rd3.place(relx=0, x=170, y=48.5, anchor=N)
        rd4.place(relx=0, x=210, y=48.5, anchor=N)
        rd5.place(relx=0, x=250, y=48.5, anchor=N)
        btn=Button(root5,text="APPLY",bg="purple",fg="white",command=show_data)
        btn.pack(side=tk.LEFT,padx=4,anchor=N)
        txt=Text(root5,width=25,height=10,wrap=WORD)
        txt.place(relx=0, x=100, y=90, anchor=N)
        MyFrame = tkinter.Frame(root5)
        MyClass(MyFrame)
        MyFrame.pack()
        root5.mainloop()


def animate():
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
    ax1=plt.axes(xlim=(0,max(t)),ylim=(min(Ry),max(Ry)))
    plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
    plt.minorticks_on()
    plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
    plt.xlabel('time')
    plt.ylabel('Ry')
    plt.figure(3)
    ax2=plt.axes(xlim=(0,max(t)),ylim=(min(Rz),max(Rz)))
    plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
    plt.minorticks_on()
    plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
    plt.xlabel('time')
    plt.ylabel('Rz')
    [line]=ax.plot([],[],lw=2)
    [line1]=ax1.plot([],[],lw=2)
    [line2]=ax2.plot([],[],lw=2)
    def init():
        line.set_data([],[])
        return([line])
    
    def animate(i):
        line.set_data(t[:i],Rx[:i])
        return([line])
    
    def init1():
        line1.set_data([],[])
        return([line1])
    
    def animate1(i):
        line1.set_data(t[:i],Ry[:i])
        return([line1])
    def init2():
        line2.set_data([],[])
        return([line2])
    
    def animate2(i):
        line2.set_data(t[:i],Rz[:i])
        return([line2])
    animation=anim.FuncAnimation(plt.figure(1),animate,init_func=init,frames=len(Rx),interval=1,
                             blit=True)

    animation1=anim.FuncAnimation(plt.figure(2),animate1,init_func=init1,frames=len(Ry),interval=1,
                             blit=True)
    animation2=anim.FuncAnimation(plt.figure(3),animate2,init_func=init2,frames=len(Rz),interval=1,
                             blit=True)
def Complementary_Filter():
    class MyClass:
        def __init__(self, frame):
            self.vata = StringVar(root4, "0") 
            self.valuesti = {"X-Axis Rotation" : "1", "Y-Axis Rotation" : "2", "Z-Axis Rotation" : "3"} 
            self.frame = frame
            
            self.fig = Figure(figsize=(11, 6), dpi=100)
            self.ax = self.fig.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
            toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
            toolbar.update()
            self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
                            
            def ShowC():
                global poilap
                poilap =int(self.vata.get())
                
                if poilap==1:
                    self.plot_graph()
                if poilap==2:
                    self.plot_graph1()
                if poilap==3:
                    self.plot_graph3()
            for (text, value) in self.valuesti.items(): 
                Radiobutton(root4, text = text, variable = self.vata, command=ShowC,value = value, indicator = 0, background = "light blue").pack(side=tk.LEFT,before=toolbar,anchor=N)
                            
                            
        def plot_graph(self):
            self.ax.cla()
            self.ax.plot(t,thetaX,"r-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('X-axis Rotation (deg)')
            self.canvas.draw()
        def plot_graph1(self):
            self.ax.cla()
            self.ax.plot(t,thetaY,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Y-axis Rotation (deg)')
            self.canvas.draw()
        def plot_graph3(self):
            self.ax.cla()
            self.ax.plot(t,thetaZ,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Z-axis Rotation(deg)')
            self.canvas.draw()
    def show_data():
      
        global pasa
        global haga
        global thetaX
        global thetaY
        global thetaZ
        
        dt=1/fs
        pasa=entry.get()
        haga=entry1.get()
        
        hpf=float(pasa)
        lpf=float(haga)
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
    global bangla            
    def on_closing():
        global bangla
        
        bangla='abnormal'
        root4.destroy()
        
  
    if bangla=='abnormal':
        root4 = Toplevel(root)
        bangla=root4.state()  
        root4.protocol("WM_DELETE_WINDOW", on_closing)
        geo=root4.geometry
        geo("+100+0")
        root4['bg'] = 'orange'
        root4.wm_title("Complementary Filter Implementation")
        label1=tk.Label(root4,justify=tk.CENTER, text="High Pass Filter Coefficient")
        label2=tk.Label(root4,justify=tk.CENTER, text="Low Pass Filter Coefficient")
        entry=Entry(root4)
        entry1=Entry(root4)

        label1.pack(side=tk.LEFT,padx=5,expand=True,anchor=N)
        entry.pack(side=tk.LEFT,padx=5,expand=True,anchor=N)
        label2.place(relx=0, x=80, y=30, anchor=N)
        entry1.place(relx=0, x=225, y=30, anchor=N)


        btn=Button(root4,text="APPLY",bg="purple",fg="white",command=show_data)
        btn.pack(side=tk.LEFT,padx=5,expand=True,anchor=N)
    
    
        MyFrame = tkinter.Frame(root4)
        MyClass(MyFrame)
        MyFrame.pack()
        root4.mainloop() 
    
def Filters():
    class MyClass:
        def __init__(self, frame):
            self.vat = StringVar(root3, "0") 
            self.valuest = {"X-Axis Acceleraion" : "1", "Y-Axis Acceleraion" : "2", "Z-Axis Acceleraion" : "3", "X-Axis FFT" : "4",  "Y-Axis FFT" : "5", "Z-Axis FFT" : "6"} 
            self.frame = frame
            
            self.fig = Figure(figsize=(11, 6), dpi=100)
            self.ax = self.fig.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
            toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
            toolbar.update()
            self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
                            
            def ShowC():
                global poila
                poila =int(self.vat.get())
                
                if poila==1:
                    self.plot_graph()
                if poila==2:
                    self.plot_graph1()
                if poila==3:
                    self.plot_graph3()
                if poila==4:
                    self.plot_Rx()
                if poila==5:
                    self.plot_Ry()
                if poila==6:
                    self.plot_Rz()
            for (text, value) in self.valuest.items(): 
                Radiobutton(root3, text = text, variable = self.vat, command=ShowC,value = value, indicator = 0, background = "light blue").pack(side=tk.LEFT,before=toolbar,anchor=N)
                            
                            
        def plot_graph(self):
            self.ax.cla()
            self.ax.plot(t,filtered,"r-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('X-Axis Acceleraion (g)')
            self.ax.set_title('X-Axis Accelerometer Filtered Data')
            self.canvas.draw()
        def plot_graph1(self):
            self.ax.cla()
            self.ax.plot(t,filtered1,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Y-Axis Acceleraion (g)')
            self.ax.set_title('Y-Axis Accelerometer Filtered Data')
            self.canvas.draw()
        def plot_graph3(self):
            self.ax.cla()
            self.ax.plot(t,filtered2,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Z-Axis Acceleraion (g)')
            self.ax.set_title('Z-Axis Accelerometer Filtered Data')
            self.canvas.draw()
        def plot_Rx(self):
            self.ax.cla()
            self.ax.semilogy(frequency,rx,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('X-Axis Acceleration FFT Plot After Filtering')
            self.canvas.draw()
        def plot_Ry(self):
            self.ax.cla()
            self.ax.semilogy(frequency,ry,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('Y-Axis Acceleration FFT Plot After Filtering')
            self.canvas.draw()
        def plot_Rz(self):
            self.ax.cla()
            self.ax.semilogy(frequency,rz,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('Z-Axis Acceleration FFT Plot After Filtering')
            self.canvas.draw()
        
    def show_data():
        print("hello")
        global pasa
        global haga
        global sos
        
        global filtered
        global filtered1
        global filtered2
        global rx,ry,rz
    
        txt.delete('0.0','end')
        pasa=entry.get()
        
        haga=var.get()
        jiji=var1.get()
        print(haga)
        if haga==1:
            haga='lp'
            melt="Low Pass Filter"
        else:
            haga='hp'
            melt="High Pass Filter"
    
        sentence="Hello,You have chosen a "+melt+" with a cut off frequency of "+pasa+" Hz.";
        txt.insert(0.0,sentence);
        hello=int(pasa)
        sos = signal.butter(10,hello,haga, fs=fs, output='sos')
        if jiji==1:
            filtered =signal.sosfilt(sos, Rx) 
        if jiji==2:
            filtered1=signal.sosfilt(sos,Ry)
        if jiji==3:
            filtered2=signal.sosfilt(sos,Rz)
        
        
        freqx_data = fft(filtered)
        lu=len(frequency)
        rx = np.abs (freqx_data [0:lu])/q
        
        freqy_data = fft(filtered1)
        ry = np.abs (freqy_data [0:lu])/q
        
        freqz_data = fft(filtered2)
        rz = np.abs (freqz_data [0:lu])/q
    
    
    
    def on_closing():
        global muta
        
        muta='abnormal'
        root3.destroy()
        
    global muta
    if muta=='abnormal':
        root3 = Toplevel(root)
        muta=root3.state()  
        root3.protocol("WM_DELETE_WINDOW", on_closing)
        geo=root3.geometry
        geo("+150+0")
        root3['bg'] = 'orange'
        root3.wm_title("Accelerometer Data Filtering")
        label1=tk.Label(root3,justify=tk.CENTER, text="Cut off Frequency:")
        label2=tk.Label(root3,justify=tk.CENTER, text="Filter Type :")
        label3=tk.Label(root3,justify=tk.CENTER, text="Select Axis to Apply Filter:")
        entry=Entry(root3)
        var=IntVar() 
        var1=IntVar() 
        rd1=Radiobutton(root3,text="Lp",variable=var,value=1)
        rd2=Radiobutton(root3,text="Hp",variable=var,value=2)
        rd3=Radiobutton(root3,text="X",variable=var1,value=1)
        rd4=Radiobutton(root3,text="Y",variable=var1,value=2)
        rd5=Radiobutton(root3,text="Z",variable=var1,value=3)
        label1.pack(side=tk.LEFT,anchor=N)
        entry.pack(side=tk.LEFT,anchor=N)
        label2.place(relx=0, x=45, y=22.5, anchor=N)
        label3.place(relx=0, x=75, y=52, anchor=N)
        rd1.place(relx=0, x=120, y=20, anchor=N)
        rd2.place(relx=0, x=200, y=20, anchor=N)
        rd3.place(relx=0, x=170, y=48.5, anchor=N)
        rd4.place(relx=0, x=210, y=48.5, anchor=N)
        rd5.place(relx=0, x=250, y=48.5, anchor=N)
        btn=Button(root3,text="APPLY",bg="purple",fg="white",command=show_data)
        btn.pack(side=tk.LEFT,padx=4,anchor=N)
        txt=Text(root3,width=25,height=10,wrap=WORD)
        txt.place(relx=0, x=100, y=90, anchor=N)
        global haga
        global pasa
    
        MyFrame = tkinter.Frame(root3)
        MyClass(MyFrame)
        MyFrame.pack()
        root3.mainloop()
                                   
    
def Timeplot():
    class MyClass:
        def __init__(self, frame):
            self.va = StringVar(root1, "0") 
            self.valuese = {"X-Axis Acceleraion" : "1", "Y-Axis Acceleraion" : "2", "Z-Axis Acceleraion" : "3", "X-Axis Gyroscope" : "4", 
                            "Y-Axis Gyroscope" : "5", "Z-Axis Gyroscope" : "6","Total Acceleration" : "7","RPM" : "8","Acceleration from RPM" : "9"} 
            self.frame = frame
            
            self.fig = Figure(figsize=(13, 6), dpi=100)
            self.ax = self.fig.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
            toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
            toolbar.update()
            self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
                            
            def ShowC():
                global poil
                poi =int(self.va.get())
                
                if poi==1:
                    self.plot_graph()
                if poi==2:
                    self.plot_graph1()
                if poi==3:
                    self.plot_graph2()
                if poi==4:
                    self.plot_graph3()
                if poi==5:
                    self.plot_graph4()
                if poi==6:
                    self.plot_graph5()
                if poi==7:
                    self.plot_graph6()
                if poi==8:
                    self.plot_graph7()
                if poi==9:
                    self.plot_graph8()
            for (text, value) in self.valuese.items(): 
                Radiobutton(root1, text = text, variable = self.va, command=ShowC,value = value, indicator = 0, background = "light blue").pack(side=tk.LEFT,before=toolbar,anchor=N)
                            
                            
        def plot_graph(self):
            self.ax.cla()
            self.ax.plot(t,Rx,"r-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('X-Axis Acceleraion (g)')
            self.ax.set_title('X-Axis Accelerometer Raw Data')
            self.canvas.draw()
        def plot_graph1(self):
            self.ax.cla()
            self.ax.plot(t,Ry,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Y-Axis Acceleraion (g)')
            self.ax.set_title('Y-Axis Accelerometer Raw Data')
            self.canvas.draw()
        def plot_graph2(self):
            self.ax.cla()
            self.ax.plot(t,Rz,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Z-Axis Acceleraion (g)')
            self.ax.set_title('Z-Axis Accelerometer Raw Data')
            self.canvas.draw()
        def plot_graph3(self):
            self.ax.cla()
            self.ax.plot(t,Gx,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('X-Axis Angular Velocity (deg/s)')
            self.ax.set_title('X-Axis Gyroscope Raw Data')
            self.canvas.draw()
        def plot_graph4(self):
            self.ax.cla()
            self.ax.plot(t,Gy,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Y-Axis Angular Velocity (deg/s)')
            self.ax.set_title('Y-Axis Gyroscope Raw Data')
            self.canvas.draw()
        def plot_graph5(self):
            self.ax.cla()
            self.ax.plot(t,Gz,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Z-Axis Angular Velocity (deg/s)')
            self.ax.set_title('Z-Axis Gyroscope Raw Data')
            self.canvas.draw()
        def plot_graph6(self):
            self.ax.cla()
            self.ax.plot(t,Tx,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Magnitude of total Acceleraion (g)')
            self.ax.set_title('Total Acceleraion Raw Data')
            self.canvas.draw()
        def plot_graph7(self):
            self.ax.cla()
            self.ax.plot(tx,p_rpm,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Revolution Per Minute')
            self.ax.set_title('RPM vs Time Plot') 
            self.canvas.draw()
        def plot_graph8(self):
            self.ax.cla()
            self.ax.plot(tx,gr,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('time (s)')
            self.ax.set_ylabel('Acceleration (g)')
            self.ax.set_title('Acceleration from RPM') 
            self.canvas.draw()
        
         
    def on_closing():
        global puta
        
        puta='abnormal'
        root1.destroy()
        
    global puta
    if puta=='abnormal':
        root1 = Toplevel(root)
        puta=root1.state()  
        root1.protocol("WM_DELETE_WINDOW", on_closing)
        geo=root1.geometry
        geo("+200+0")
        root1['bg'] = 'orange'
        root1.wm_title("Time Domain Plot")
        MyFrame = tkinter.Frame(root1)
        MyClass(MyFrame)
        MyFrame.pack()
        root1.mainloop() 
                      

def FFT():
    class MyClass:
        def __init__(self, frame):
            self.vac = StringVar(root2, "0") 
            self.valuesel = {"X-Axis Acceleraion" : "1", "Y-Axis Acceleraion" : "2", "Z-Axis Acceleraion" : "3", "X-Axis Gyroscope" : "4",  "Y-Axis Gyroscope" : "5", "Z-Axis Gyroscope" : "6"} 
            self.frame = frame
            self.fig = Figure(figsize=(11, 6), dpi=100)
            self.ax = self.fig.add_subplot(111)
            
            self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
            toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
            toolbar.update()
            self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
                            
            def ShowCc():
                global poil
                poil =int(self.vac.get())
                
                if poil==1:
                    self.plot_graph()
                if poil==2:
                    self.plot_graph1()
                if poil==3:
                    self.plot_graph3()
                if poil==4:
                    self.plot_Gx()
                if poil==5:
                    self.plot_Gy()
                if poil==6:
                    self.plot_Gz()
            for (text, value) in self.valuesel.items(): 
                Radiobutton(root2, text = text, variable = self.vac, command=ShowCc,value = value, indicator = 0, background = "light blue").pack(side=tk.LEFT,before=toolbar,anchor=N)
                            
                            
        def plot_graph(self):
            self.ax.cla()
            self.ax.semilogy(frequency,y,"r-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('X-Axis Acceleration FFT Plot')
            self.canvas.draw()
        def plot_graph1(self):
            self.ax.cla()
            self.ax.semilogy(frequency,z,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('Y-Axis Acceleration FFT Plot')
            self.canvas.draw()
        def plot_graph3(self):
            self.ax.cla()
            self.ax.semilogy(frequency,m,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('Z-Axis Acceleration FFT Plot')
            self.canvas.draw()
        def plot_Gx(self):
            self.ax.cla()
            self.ax.semilogy(frequency,gx,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('X-Axis Gyroscope FFT Plot')
            self.canvas.draw()
        def plot_Gy(self):
            self.ax.cla()
            self.ax.semilogy(frequency,gy,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('Y-Axis Gyroscope FFT Plot')
            self.canvas.draw()
        def plot_Gz(self):
            self.ax.cla()
            self.ax.semilogy(frequency,gz,"b-*")
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],linestyle='-',linewidth=2)
            self.ax.minorticks_on()
            self.ax.grid(axis='both',which='major',color=[166/255,166/255,166/255],
                                       linestyle='-',linewidth=2)
            self.ax.set_xlabel('Frequency (Hz)')
            self.ax.set_ylabel('Magnitude (dB)')
            self.ax.set_title('Z-Axis Acceleration FFT Plot')
            self.canvas.draw()

            
    def on_closing():
        global jhuta
        
        jhuta='abnormal'
        root2.destroy()
    global jhuta
    if jhuta=='abnormal':
        root2 = Toplevel(root)
        jhuta=root2.state()  
        root2.protocol("WM_DELETE_WINDOW", on_closing)
        geo=root2.geometry
        geo("+400+0")
        root2['bg'] = 'orange'
        root2.wm_title("FFT Plot")
        MyFrame = tkinter.Frame(root2)
        MyClass(MyFrame)
        MyFrame.pack()
        root2.mainloop() 

class OptionsWindow(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        pass


class MainWindow(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.options_toplevel = None
        
        
        tk.Button(self, text='Select', command=self._open_toplevel).pack()

    def _open_toplevel(self,master=None, *args):
        if self.options_toplevel is None:
            self.options_toplevel = tk.Toplevel(self.master)
            self.options_toplevel.geometry("800x800+800+300")
            self.options_toplevel.protocol('WM_DELETE_WINDOW', self.on_tl_close)
            gui = OptionsWindow(self.options_toplevel)
            gui.pack()
            self.options_toplevel.geometry("350x280") 
            self.options_toplevel.title("Analysis Tools")
            global muta
            global puta
            global nuta
            global khuta
            global jhuta
            global bangla
            global dhaka
            jhuta='abnormal'
            muta='abnormal'
            puta='abnormal'
            nuta='abnormal'
            khuta='abnormal'
            bangla='abnormal'
            dhaka='abnormal'
            v = StringVar(self.options_toplevel, "0") 
            values = {"Time Plot" : "1", 
          "Frequency Plot" : "2", 
          "Accelorometer Data Filtering" : "3", 
          "Gyroscope Data Filtering" : "4",
          "Complementary Filter" : "5","Data Comparison" : "6", "Real Time Data Plot" : "7", "Save Data" : "8"}
            def ShowChoice():
                global po
                
                po =int(v.get())
              
                if po==1:
                    Timeplot()
#                   
                if po==2:
                    FFT()
#                   
                if po==3:
                    Filters()
                if po==4:
                    Filters1()
                if po==5:
                    Complementary_Filter()
                if po==6:
                    Data_Comparison()
                if po==7:
                    animate()
                if po==8:
                    save()
#            
            for (text, value) in values.items(): 
                Radiobutton(self.options_toplevel, text = text, variable = v, command=ShowChoice,value = value, indicator = 0, background = "light blue").pack(fill = X, ipady = 5)


    def on_tl_close(self, *args):
        self.options_toplevel.destroy()
        self.options_toplevel = None


root = tk.Tk()
root.wm_state('iconic')
root.wm_title("File Selection and Display")
label1=tk.Label(root,justify=tk.LEFT,
              padx = 10, text="Select a text file:")
label1.place(relx=0, x=50, y=0, anchor=N)
geo=root.geometry
geo("400x400+200+300")
root['bg'] = 'salmon'
flist = os.listdir()
 
lbox = tk.Listbox(root)
lbox.pack()
for item in flist:
    lbox.insert(tk.END, item)



window = Toplevel(root)
window.after(5000, lambda: window.destroy()) 
label_one = tk.Label(window,bg="gray61", justify=tk.LEFT,
              padx = 10,text = 'Welcome to Acceleration Avionics Performance Analysis Tool')

label_two = tk.Label(window,bg="gray61", justify=tk.LEFT,
              padx = 10,text = 'Developed by Mohammad Nazibul Hassan ')
label_one.pack(side=tk.TOP,anchor=N)
label_two.pack(side=tk.TOP,anchor=N)
geo=window.geometry
geo("1500x850+0+0")
window['bg'] = 'gray61'
window.wm_title("Hola!")
label_one.config(font=("Courier", 30))
label_two.config(font=("Courier", 30))
#path = "image.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))
img = ImageTk.PhotoImage(file="sensor_1.jpg")
#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)
##
###The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom",after=label_one, expand = "yes")

 
def showcontent(event):
    global data
    global niva
    global t
    global q
    global Rx
    global Ry
    global Rz
    global Gx
    global Gy
    global Gz
    global Tx
    global fs
    global fsh
    global frequency
    global y,z,m,gy,gx,gz
    
    fs=1000
    fsh=500
    x = lbox.curselection()[0]
    file = lbox.get(x)
    with open(file) as file:
        file = file.read()
    data=lbox.get(x) 
    niva=np.genfromtxt(data,delimiter=',',usecols=np.arange(0,15))
    A=niva[0:,0]
    B=niva[0:,1]
    C=niva[0:,2]
    Rx=A
    Ry=B
    Rz=C
    D=niva[0:,3]
    E=niva[0:,4]
    F=niva[0:,5]
    Gx=D
    Gy=E
    Gz=F
    G=niva[0:,8]
    H=niva[0:,9]
    I=niva[0:,10]
    J=niva[0:,11]
    K=niva[0:,12]
    L=niva[0:,13]
    M=niva[0:,14]
    lili=len(A)
    for i in range(lili):
        value= (int(A[i])<<8)|int(B[i])
        value1=(int(C[i])<<8)|int(D[i])
        value2=(int(E[i])<<8)|int(F[i])
    
        value3= (int(G[i])<<8)|int(H[i])
        value4=(int(I[i])<<8)|int(J[i])
        value5=(int(K[i])<<8)|int(L[i])
    
        if(value1>32768):
            value1=value1-65536
        if(value>32768):
            value=value-65536
        if(value2>32768):
            value2=value2-65536
        if(value3>32768):
            value3=value3-65536
        if(value4>32768):
            value4=value4-65536
        if(value5>32768):
            value5=value5-65536
        if int(M[i])==0:
        
            Rx[i]=value/16384
            Ry[i]=value1/16384
            Rz[i]=value2/16384
            Gx[i]=value3/131.2
            Gy[i]=value4/131.2
            Gz[i]=value5/131.2
        if int(M[i])==1:
            
            Rx[i]=value/8192
            Ry[i]=value1/8192
            Rz[i]=value2/8192
            Gx[i]=value3/131.2
            Gy[i]=value4/131.2
            Gz[i]=value5/131.2
        if int(M[i])==2:
          
            Rx[i]=value/4096
            Ry[i]=value1/4096
            Rz[i]=value2/4096
            Gx[i]=value3/131.2
            Gy[i]=value4/131.2
            Gz[i]=value5/131.2
        if int(M[i])==3:
            
            Rx[i]=value/2048
            Ry[i]=value1/2048
            Rz[i]=value2/2048
            Gx[i]=value3/131.2
            Gy[i]=value4/131.2
            Gz[i]=value5/131.2
        
        Rx[i]=value/8192
        Ry[i]=value1/8192
        Rz[i]=value2/8192
        Gx[i]=value3/131
        Gy[i]=value4/131
        Gz[i]=value5/131
    Fx=np.square(Rx)       
    Fy=np.square(Ry)
    Fz=np.square(Rz)
    Ft=Fx+Fy+Fz
    Tx=np.sqrt(Ft)

    q=len(Rx)
    t = np.arange(q) /fs
    
    frequency = np.linspace(0, 1, np.fix(q/2))*fsh
    freq_data = fft(Rx)
    ha=len(frequency)
    
    y = np.abs (freq_data [0:ha])/q
    
    freq_data1 = fft(Ry)
    ka=len(frequency)
    
    z = np.abs (freq_data1 [0:ka])/q
    
    freq_data2 = fft(Rz)
    la=len(frequency)
    
    m = np.abs (freq_data2 [0:la])/q
    
    freq_data3 = fft(Gx)
    na=len(frequency)
    
    gx = np.abs (freq_data3 [0:na])/q
    
    freq_data4= fft(Gy)
    pa=len(frequency)
    
    gy = np.abs (freq_data4 [0:pa])/q
    
    freq_data5 = fft(Gz)
    awa=len(frequency)
    
    gz = np.abs (freq_data5 [0:awa])/q
    
    text.delete('1.0', tk.END)
    text.insert(tk.END, file)
 
gui = MainWindow(root)
gui.pack() 
text = tk.Text(root, bg='cyan')
text.pack()
 
lbox.bind("<<ListboxSelect>>", showcontent)

root.mainloop()