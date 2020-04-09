# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:48:08 2020

@author: Nazibul
"""

from tkinter import *
from tkinter import messagebox

def callback():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        print("hello")

root = Tk()
root.protocol("WM_DELETE_WINDOW", callback)

root.mainloop()