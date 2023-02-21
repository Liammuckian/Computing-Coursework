import tkinter as tk
from tkinter import ttk

class Widget():
    def __init__(self,parent, r, c, text):
        self.parent = parent
        self.r = r
        self.c = c
        self.text = text
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.W}
        self.label = ttk.Label(self.parent, text = self.text)
        self.label.grid(row = self.r, column = self.c, **gridOptions)
        self.entryVariable = tk.StringVar()
        self.entry = ttk.Entry(self.parent, textvariable=self.entryVariable)
        self.entry.grid(row = self.r, column = self.c+1, **gridOptions)