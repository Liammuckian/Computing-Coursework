import tkinter as tk
from tkinter import ttk

class label():
    def __init__(self,parent, r, c, text):
        self.parent = parent
        self.r = r
        self.c = c
        self.text = text
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.W}
        self.label = ttk.Label(self.parent, text = self.text)
        self.label.grid(row = self.r, column = self.c, **gridOptions)