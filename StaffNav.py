import tkinter as tk
from tkinter import ttk
import os

class StaffNavBar():
    # Read the navigation buttons from the file "navbuttons.txt"
    with open (os.path.dirname(os.getcwd())+"//Coursework//Staff//staffnav.txt") as f:
        NAV_BUTTONS =[line.strip() for line in f.readlines()]
        
    def __init__(self, window, parent):
        # Initialize the navigation bar object
        self.window = window
        self.parent = parent
        self.holdingFrame = ttk.Frame(self.parent)
        # Add the frame to the parent widget
        self.holdingFrame.grid(row =0, column = 0,columnspan = 5,  padx = 5, pady = 5)
        self.c = 0
        # Create a navigation button for each button in the list
        for i in range(0, len(StaffNavBar.NAV_BUTTONS)):
            navButton = ttk.Button(self.holdingFrame, text = StaffNavBar.NAV_BUTTONS[i],command = lambda x=i:self.window.show_frame(x))
            navButton.grid(row = 0, column = self.c, padx = 5, pady = 5)
            self.c+=1
                       
if __name__=="__main__":
    window = tk.Tk()
    nav = StaffNavBar(window, window)
    window.mainloop()
