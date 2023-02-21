import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from basic_wid import Widget
from custom_list import MyListBox
from Customer.CustomerNav import CustomerNavBar
from database import *
from crud import *

class screen1(ttk.LabelFrame):
    def __init__(self, window, title):
        super().__init__(window)
        self.window = window
        self.title = title
        self['text'] = self.title

        # Set grid options for the LabelFrame
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.W}      
        self.grid(row = 0, column = 0, **gridOptions)

        # Add the navigation bar
        self.navigation = CustomerNavBar(self.window, self)

        # Connect to the database and retrieve data and fields
        self.myDB = DataBase("mydatabase.db") 
        fields = self.myDB.get_fields("RESERVATIONS") 
        self.data = self.myDB.fetch_all("Reservations")

        # Populate the LabelFrame with fields
        self.populate(fields)

        # Add a listbox to display reservations
        self.ReservationList = MyListBox(self, 6, 0, "mydatabase.db", "RESERVATIONS")

        # Add a CRUD button widget to allow the user to search for reservations
        self.crudButtonWidget = CRUD(self,self.ReservationList,"mydatabase.db", "RESERVATIONS", 7, 0, [])


    # Add widgets for each field in the LabelFrame
    def populate(self, fieldNames):
        r, c = 1, 0
        for i in range(0, len(fieldNames)):
            Widget(self, r, c, fieldNames[i])
            r+=1

# Create a test window and add a screen1 LabelFrame to it
if __name__=="__main__":
    testWindow = tk.Tk()
    testFrame = screen1(testWindow, "Reservations")
    testWindow.mainloop()
