import tkinter as tk
from tkinter import ttk
from Staff.StaffHome import *
from Staff.StaffReservations import *
from Staff.StaffSchedule import *
from Staff.StaffAccount import *

class App(tk.Tk):
    def __init__(self):
        # Initialize the Tkinter application
        super().__init__()

        # Create a list of frame instances
        self.frames = [Home(self, "Staff View"),
                       screen1(self, "Staff View"),
                       screen2(self, "Staff View"),
                       screen3(self, "Staff View")
                       ]
        # Show the first frame in the list
        self.show_frame(0)
        
    def show_frame(self, frame_num):
        # Get the frame to show from the list of frames
        frame_to_show = self.frames[frame_num]
        # Raise the selected frame to the top of the display stack
        frame_to_show.tkraise()

if __name__=="__main__":
    # Create an instance of the application
    myApp = App()
    # Run the main event loop of the Tkinter application
    myApp.mainloop() 