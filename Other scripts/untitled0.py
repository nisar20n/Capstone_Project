#from tkinter import *
#
#def firstFrame(window):
#    global first_frame
#    first_frame = Frame(window)
#    first_frame.place(in_=window, anchor="c", relx=.5, rely=.5)
#    Label(first_frame, text="ATTENTION !").grid(row=1,column=1,columnspan=3)
#
#
#def secondFrame(window):
#    global second_frame
#    second_frame= Frame(window, highlightthickness=3)
#    second_frame.place(in_=window, anchor="c", relx=.5, rely=.5)
#    Label(second_frame, text="This is second frame.").grid(row=1, column=1, columnspan=3, padx=25, pady=(15, 0))
#
#
#window = Tk()
#window.title('Some Title')
#window.attributes("-fullscreen", False)
#window.resizable(width=True, height=True)
#window.geometry('300x200')
#
#
#firstFrame(window)
#secondFrame(window)
#first_frame.tkraise()
#window.after(5000, lambda: first_frame.destroy()) # you can try different things here
#window.mainloop()
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        print("hello")
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()