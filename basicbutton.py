import tkinter as tk
from tkinter import ttk

class button():
    def __init__(self,parent, r, c, text, buttoncommand):
        self.parent = parent
        self.r = r
        self.c = c
        self.text = text
        self.buttoncommand = buttoncommand
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.W}
        self.button = ttk.Button(self.parent, text = self.text, command=self.buttoncommand)
        self.button.grid(row = self.r, column = self.c, **gridOptions)