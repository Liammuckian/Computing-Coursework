import tkinter as tk
from tkinter import ttk
from Manager.navBar import NavBar
from database import *
from Label import *
from custom_list import *
from crud import *

import tkinter as tk
from tkinter import ttk

class Home(ttk.LabelFrame):
    def __init__(self, window, title):
        # Initialize the label frame
        super().__init__(window)
        # Set the window and title as instance variables
        self.window = window
        self.title = title
        # Set the label frame's text to the given title
        self['text'] = self.title
        
        # Set the grid options for the label frame's layout
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.NSEW}
        # Use the grid layout manager to place the label frame in the window
        self.grid(row = 0, column = 0, **gridOptions)

        # Create an instance of a database
        self.myDB = DataBase("mydatabase.db")
        # Create an instance of a navigation bar
        self.navigation = NavBar(self.window, self)
        # Create a "Welcome" label widget and place it in the label frame
        self.WelcomeLabel = label(self, 1, 0, "Welcome back! Hope you have a good day! :)")
        # Create a "Time" label widget and place it in the label frame
        self.TimeLabel = label(self, 2, 0, "Open 9am-10pm")
        # Retrieve average rating data from the database
        self.AverageRatings = self.myDB.AverageData("REVIEWS", "RATING")
        # Extract the average rating from the tuple
        self.TupleRating = self.AverageRatings[0]
        self.AverageRating = float(self.TupleRating[0])
        # Create a "Rating" label widget and place it in the label frame
        self.RatingLabel = label(self, 3, 0, f"Restuarant rating:{self.AverageRating}") 
    
if __name__=="__main__":
    # Create a test window
    testWindow = tk.Tk()
    # Create a test label frame with the test window as the parent and "Home" as the title
    testFrame = Home(testWindow, "Home")
    # Run the main event loop of the GUI application
    testWindow.mainloop()
