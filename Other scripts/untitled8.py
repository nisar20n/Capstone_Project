# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:33:37 2020

@author: Nazibul
"""
import tkinter as tk


class OptionsWindow(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        pass


class MainWindow(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.options_toplevel = None
        tk.Button(self, text='open toplevel', command=self._open_toplevel).pack()

    def _open_toplevel(self, *args):
        if self.options_toplevel is None:
            self.options_toplevel = tk.Toplevel(self.master)
            self.options_toplevel.protocol('WM_DELETE_WINDOW', self.on_tl_close)
            gui = OptionsWindow(self.options_toplevel, width=300, height=300)
            gui.pack()

    def on_tl_close(self, *args):
        self.options_toplevel.destroy()
        self.options_toplevel = None


root = tk.Tk()
gui = MainWindow(root)
gui.pack()
root.mainloop()