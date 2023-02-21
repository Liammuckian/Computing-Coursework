import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from basic_wid import Widget
from custom_list import MyListBox
from Staff.StaffNav import StaffNavBar
from database import *
from crud import *

# Define a class 'screen1' that inherits from 'ttk.LabelFrame'
class screen1(ttk.LabelFrame):
    
    # Define an initializer method that takes 'window' and 'title' as arguments
    def __init__(self, window, title):
        # Call the initializer method of the parent class 'ttk.LabelFrame'
        super().__init__(window)
        # Set the 'window' and 'title' attributes
        self.window = window
        self.title = title
        # Set the text of the 'ttk.LabelFrame' to the given title
        self['text'] = self.title
        # Define grid options
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.W}      
        # Add the 'ttk.LabelFrame' to the grid with the specified options
        self.grid(row = 0, column = 0, **gridOptions)
        # Add a navigation bar to the window
        self.navigation = StaffNavBar(self.window, self)
        # Create a database connection and get the list of fields for the 'RESERVATIONS' table
        self.myDB = DataBase("mydatabase.db") 
        fields = self.myDB.get_fields("RESERVATIONS") 
        # Fetch all the data from the 'Reservations' table
        self.data = self.myDB.fetch_all("Reservations")
        # Populate the 'ttk.LabelFrame' with the field names from the 'RESERVATIONS' table
        self.populate(fields)
        # Create a listbox to display the reservations and a CRUD button widget for updating, deleting and adding reservations
        self.ReservationList = MyListBox(self, 6, 0, "mydatabase.db", "RESERVATIONS")
        self.crudButtonWidget = CRUD(self, self.ReservationList, "mydatabase.db", "RESERVATIONS", 7, 0, ["Update", "Delete", "New"])

    # Define a method to populate the 'ttk.LabelFrame' with field names
    def populate(self, fieldNames):
        r, c = 1, 0
        # Add a label for each field name to the 'ttk.LabelFrame'
        for i in range(0, len(fieldNames)):
            Widget(self, r, c, fieldNames[i])
            r+=1

# Create a test window and a 'screen1' instance to add to it
if __name__=="__main__":
    testWindow = tk.Tk()
    testFrame = screen1(testWindow, "Reservations")
    testWindow.mainloop()
