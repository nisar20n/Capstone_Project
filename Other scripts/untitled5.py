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

def create_window():
    
    global m
    
    
    master = Toplevel(root) 
   
    master.protocol('WM_DELETE_WINDOW', self.on_tl_close) 
    m=tk.Toplevel.winfo_exists(root)
    m=m+1
    print(m) 
    master.geometry("175x175") 
    v = StringVar(master, "1") 
    values = {"Time Plot" : "1", 
          "Frequency Plot" : "2", 
          "Filter Selection" : "3", 
          "Filtered Data" : "4", 
          "Complementary Filter" : "5"} 
    
    def ShowChoice():
        global po
        po =int(v.get())
        if po==1:
            plt.figure(2)
            plt.plot(t,Rx,"b-*")
            plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
            plt.minorticks_on()
            plt.grid(axis='both',which='major',color=[166/255,166/255,166/255],
         linestyle='-',linewidth=2)
            plt.xlabel('time')
            plt.ylabel('Rx')
 
        if po==2:
            mas = Tk() 
        if po==3:
            mast = Tk() 
            
    for (text, value) in values.items(): 
        Radiobutton(master, text = text, variable = v, command=ShowChoice,value = value, indicator = 0, background = "light blue").pack(fill = X, ipady = 5)
    
global master

root = tk.Tk()
geo=root.geometry
geo("400x400+400+400")
root['bg'] = 'orange'

flist = os.listdir()
def close_window ():
    global killa
    killa=pi+1;

lbox = tk.Listbox(root)
lbox.pack()
button = tk.Button(text = "Click and Quit", command = create_window)
button.pack()

#b = tk.Button(root, text="Create new window", command=root.quit())
#b.pack()
# THE ITEMS INSERTED WITH A LOOP
for item in flist:
    lbox.insert(tk.END, item)


 
def showcontent(event):
    global data
    global niva
    global t
    global Rx
    global Ry
    global Rz
    global Gx
    global Gy
    global Gz
  
    x = lbox.curselection()[0]
    file = lbox.get(x)
    with open(file) as file:
        file = file.read()
    data=lbox.get(x) 
    niva=np.genfromtxt(data,delimiter=',')
    Rx=niva[1:,0]
    Ry=niva[1:,1]
    Rz=niva[1:,2]
    Gx=niva[1:,3]
    Gy=niva[1:,4]
    Gz=niva[1:,5]
    avg1=np.mean(Rx,0)
    avg2=np.mean(Ry,0)
    avg3=np.mean(Rz,0)
    x=len(Rx)
    t = np.arange(x) /80
    text.delete('1.0', tk.END)
    text.insert(tk.END, file)
 
 
text = tk.Text(root, bg='cyan')
text.pack()
 
lbox.bind("<<ListboxSelect>>", showcontent)


root.mainloop()

