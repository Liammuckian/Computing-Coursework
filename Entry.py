import tkinter as tk
from tkinter import ttk

class entry():
    def __init__(self,parent, r, c, textvariable):
        self.parent = parent
        self.r = r
        self.c = c
        self.textvariable = textvariable
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.W}
        self.label = ttk.Entry(self.parent, textvariable = self.textvariable)
        self.label.grid(row = self.r, column = self.c, **gridOptions)