import tkinter as tk
from tkinter import ttk
from Customer.CustomerHome import *
from Customer.CustomerReservations import *
from Customer.CustomerReviews import *
from Customer.CustomerMenu import *

# Define the App class that inherits from tk.Tk
class App(tk.Tk):
    # Initialize the App class
    def __init__(self):
        # Call the __init__ method of the parent class tk.Tk
        super().__init__()
        
        # Create a list of frames to display within the App
        self.frames = [Home(self, "Customer View"),
                       screen1(self, "Customer View"),
                       screen2(self, "Customer View"),
                       screen3(self, "Customer View")
                       ]
        
        # Show the first frame in the list
        self.show_frame(0)
        
    # Method to show a specified frame in the App
    def show_frame(self, frame_num):
        # Get the frame to show from the list of frames
        frame_to_show = self.frames[frame_num]
        # Raise the specified frame to the top of the display stack
        frame_to_show.tkraise()

if __name__=="__main__":
    # Create an instance of the App class
    MyApp = App()
    # Start the main event loop of the Tkinter window
    MyApp.mainloop()