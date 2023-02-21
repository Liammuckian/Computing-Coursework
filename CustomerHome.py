import tkinter as tk
from tkinter import ttk
from Customer.CustomerNav import CustomerNavBar
from database import *
from Label import *
from custom_list import *
from crud import *
from basicbutton import *

# Define the Home class that inherits from ttk.LabelFrame
class Home(ttk.LabelFrame):
    # Initialize the Home class with the window and title arguments
    def __init__(self, window, title):
        # Call the __init__ method of the parent class ttk.LabelFrame
        super().__init__(window)
        
        # Assign the window and title arguments to class variables
        self.window = window
        self.title = title
        
        # Set the text displayed on the ttk.LabelFrame
        self['text'] = self.title
        
        # Define the grid options to position the ttk.LabelFrame within its parent widget
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.NSEW}
        # Position the ttk.LabelFrame within its parent widget
        self.grid(row = 0, column = 0, **gridOptions)

        # Initialize a DataBase object with the database file "mydatabase.db"
        self.myDB = DataBase("mydatabase.db")
        # Initialize a CustomerNavBar object with the window and Home class as arguments
        self.navigation = CustomerNavBar(self.window, self)
        # Initialize several label objects with text and positions specified
        self.WelcomeLabel = label(self, 1, 0, "Welcome back! Hope you have a good day! :)")
        self.TimeLabel = label(self, 2, 0, "Open 9am-10pm")
        # Calculate the average restaurant rating and assign it to a class variable
        self.AverageRatings = self.myDB.AverageData("REVIEWS", "RATING")
        self.TupleRating = self.AverageRatings[0]
        self.AverageRating = float(self.TupleRating[0])
        # Initialize a label object that displays the average rating
        self.RatingLabel = label(self, 3, 0, f"Restuarant rating:{self.AverageRating}") 
        self.CallButton = button(self.window, 2, 3, "Call Restaurant", lambda:Home.CallCommand(self))

    def CallCommand(self):
        # Create a new window to call restaurant
        self.newwindow = tk.Toplevel(self.window)
        self.newwindow.title("Call")
        
        # Define grid options for layout
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.NSEW}      
        self.grid(row = 0, column = 0, **gridOptions)
        self.WelcomeLabel = label(self.newwindow, 1, 0, "Now calling Restaurant...")
    
if __name__=="__main__":
    # Create a Tkinter window
    testWindow = tk.Tk()
    # Create an instance of the Home class with the window and "Home" as arguments
    testFrame = Home(testWindow, "Home")
    # Start the main event loop of the Tkinter window
    testWindow.mainloop()