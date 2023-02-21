import tkinter as tk
from tkinter import ttk
from Manager.navBar import NavBar
from database import *
from basic_wid import *
from custom_list import *
from crud import *
from basicbutton import *

class screen2(ttk.LabelFrame):
    def __init__(self, window, title):
        super().__init__(window)
        self.window = window
        self.title = title
        self['text'] = self.title
        
        # Define grid options for layout
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.NSEW}      
        self.grid(row = 0, column = 0, **gridOptions)

        # Create a navigation bar
        self.navigation = NavBar(self.window, self)

        # Connect to database and fetch data
        self.myDB = DataBase("mydatabase.db")  
        fields = self.myDB.get_fields("STAFF")  
        self.data = self.myDB.fetch_all("Staff")

        # Populate the screen with data
        self.populate(fields)

        # Create a listbox to display the data
        self.StaffList = MyListBox(self, 6, 0, "mydatabase.db", "STAFF")

        # Add CRUD buttons to manipulate the data
        self.crudButtonWidget = CRUD(self, self.StaffList, "mydatabase.db", "STAFF", 7, 0, ["Update", "Delete", "New"])

        # Create a button to view the staff rota
        self.ShiftButton = button(self, 1, 3, "View rota", lambda:self.RotaCommand(window))
        
    def RotaCommand(self, window):
        # Create a new window to display the rota
        self.newwindow = tk.Toplevel(window)
        self.newwindow.title("Rota")
        
        # Define grid options for layout
        gridOptions = {'padx':5, 'pady':5, 'sticky':tk.NSEW}      
        self.grid(row = 0, column = 0, **gridOptions)

        # Create a navigation bar for the new window
        self.navigation = NavBar(self.newwindow, self)

        # Connect to database and fetch data
        self.myDB = DataBase("mydatabase.db") 
        fields = self.myDB.get_fields("SHIFTS") 
        self.data = self.myDB.fetch_all("Shifts")

        # Populate the new window with data
        self.populate2(self.newwindow, fields)

        # Create a listbox to display the data
        self.StaffList = MyListBox(self.newwindow, 6, 0, "mydatabase.db", "SHIFTS")

        # Add CRUD buttons to manipulate the data
        self.crudButtonWidget = CRUD(self.newwindow, self.StaffList, "mydatabase.db", "SHIFTS", 7, 0, ["Update", "Delete", "New"])
        

    def populate(self, fieldNames):
        # Populate the screen with labels for each field
        r, c = 1, 0
        for i in range(0, len(fieldNames)):
            Widget(self, r, c, fieldNames[i])
            r += 1

    def populate2(self, parent, fieldNames):
        # Populate the new window with labels for each field
        r, c = 1, 0
        for i in range(0, len(fieldNames)):
            Widget(parent, r, c, fieldNames[i])
            r += 1

if __name__=="__main__":
    # Create a test window to display the screen
    testWindow = tk.Tk()
    testFrame = screen2(testWindow, "Staff")
    testWindow.mainloop()