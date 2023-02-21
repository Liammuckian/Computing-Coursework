import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from basic_wid import Widget
from custom_list import MyListBox
from Staff.StaffNav import StaffNavBar
from database import *
from crud import *

# Define the screen2 class that inherits from ttk.LabelFrame
class screen2(ttk.LabelFrame):
    # Constructor that initializes the class
    def __init__(self, window, title):
        # Call the superclass's constructor and pass in the window
        super().__init__(window)
        self.window = window
        self.title = title
        # Set the text of the label frame to the given title
        self['text'] = self.title
        
        # Set options for the grid layout
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.W}      
        # Add the label frame to the grid
        self.grid(row = 0, column = 0, **gridOptions)

        # Add a navigation bar to the label frame
        self.navigation = StaffNavBar(self.window, self)
        
        # Create a database object for the 'SHIFTS' table and retrieve its fields and data
        self.myDB = DataBase("mydatabase.db") 
        fields = self.myDB.get_fields("SHIFTS") 
        self.data = self.myDB.fetch_all("Shifts")
        
        # Populate the label frame with widgets using the retrieved fields
        self.populate(fields)
        # Add a listbox to the label frame for the 'SHIFTS' table
        self.ReservationList = MyListBox(self, 6, 0, "mydatabase.db", "SHIFTS")
        # Add a CRUD widget to the label frame for the 'SHIFTS' table
        self.crudButtonWidget = CRUD(self,self.ReservationList,"mydatabase.db", "SHIFTS", 7, 0, [])

    # Method to populate the label frame with widgets
    def populate(self, fieldNames):
        r, c = 1, 0
        # Loop through the field names and add a widget for each one to the label frame
        for i in range(0, len(fieldNames)):
            Widget(self, r, c, fieldNames[i])
            r+=1

# If this is the main module being run, create a test window and the screen2 object
if __name__=="__main__":
    testWindow = tk.Tk()
    testFrame = screen2(testWindow, "Shifts")
    testWindow.mainloop()



