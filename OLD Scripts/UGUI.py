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
    root1 = tk.Tk()
#    geo=root1.geometry
#    geo("400x400+400+400")
#    root1['bg'] = 'orange'
#    root1.title("Graphical Tools")
   
    v = tk.IntVar()
    v.set(1)  # initializing the choice, i.e. Python

    languages = [("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]
    

    def ShowChoice():
        print(v.get())

    tk.Label(root1, 
         text="""Choose your favourite 
         programming language:""",
         justify = tk.LEFT,
         padx = 20).pack()
    for val, language in enumerate(languages):
        tk.Radiobutton(root1,text=language,indicatoron = 0,width = 20,padx = 20,variable=v,command=ShowChoice,
        value=val).pack(anchor=tk.W)
    root1.mainloop()
#    T.pack()
#    T.insert(tk.END, data)
    

root = tk.Tk()
label1=Label(root,text="Cut off Frequency")
label2=Label(root,text="Filter Type")
geo=root.geometry
geo("400x400+400+400")
root['bg'] = 'orange'
root.title("File Selection")

flist = os.listdir()
def close_window ():
    global killa
    killa=pi+1;

lbox = tk.Listbox(root)
lbox.pack()
button = tk.Button(text = "Select File", command = create_window)
button.pack()
#b = tk.Button(root, text="Create new window", command=root.quit())
#b.pack()
# THE ITEMS INSERTED WITH A LOOP
for item in flist:
    lbox.insert(tk.END, item)


 
def showcontent(event):
    global data
    global niva
  
    x = lbox.curselection()[0]
    file = lbox.get(x)
    with open(file) as file:
        file = file.read()
    data=lbox.get(x) 
    niva=np.genfromtxt(data,delimiter=',')
    text.delete('1.0', tk.END)
    text.insert(tk.END, file)
 
 
text = tk.Text(root, bg='cyan')

text.pack()

 
lbox.bind("<<ListboxSelect>>", showcontent)


root.mainloop()

