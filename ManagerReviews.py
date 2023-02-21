import tkinter as tk
from tkinter import ttk
from Manager.navBar import NavBar
from database import *
from basic_wid import *
from custom_list import *
from crud import *
from Label import *


class screen3(ttk.LabelFrame):
    """A class to create frame objects used in an App"""

    def __init__(self, window, title):
        super().__init__(window)
        self.window = window
        self.title = title
        self['text'] = self.title
        # Set grid options for the LabelFrame
        gridOptions = {'padx': 5, 'pady': 5, 'sticky': tk.NSEW}
        self.grid(row=0, column=0, **gridOptions)
        # Add the navigation bar
        self.navigation = NavBar(self.window, self)
        # Connect to the database and retrieve data and fields
        self.myDB = DataBase("mydatabase.db")  
        fields = self.myDB.get_fields("REVIEWS")  
        self.data = self.myDB.fetch_all("Reviews")
        # Populate the LabelFrame with fields
        self.populate(fields)
        # Add a listbox to display reviews
        self.ReviewList = MyListBox(self, 6, 0, "mydatabase.db", "REVIEWS")
        # Add a CRUD button widget to allow the user to view reservations
        self.crudButtonWidget = CRUD(self, self.ReviewList, "mydatabase.db", "REVIEWS", 7, 0, [])
        # Calculate the average restaurant rating and assign it to a class variable
        self.AverageRatings = self.myDB.AverageData("REVIEWS", "RATING")
        self.TupleRating = self.AverageRatings[0]
        self.AverageRating = float(self.TupleRating[0])
        # Initialize a label object that displays the average rating
        self.RatingLabel = label(self, 1, 3, f"Restuarant rating:{self.AverageRating}") 

    # Add widgets for each field in the LabelFrame
    def populate(self, fieldNames):
        r, c = 1, 0
        for i in range(0, len(fieldNames)):
            Widget(self, r, c, fieldNames[i])
            r += 1

# Create a test window and add a screen2 LabelFrame to it
if __name__ == "__main__":
    testWindow = tk.Tk()
    testFrame = screen3(testWindow, "Reviews")
    testWindow.mainloop()
