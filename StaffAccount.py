import tkinter as tk
from tkinter import ttk
from Staff.StaffNav import StaffNavBar
from database import *
from basic_wid import *
from custom_list import *
from crud import *


class screen3(ttk.LabelFrame):
    def __init__(self, window, title):
        super().__init__(window)
        self.window = window
        self.title = title
        self['text'] = self.title
        # Set grid options for the LabelFrame
        gridOptions = {'padx': 5, 'pady': 5, 'sticky': tk.NSEW}
        self.grid(row=0, column=0, **gridOptions)
        # Add the navigation bar
        self.navigation = StaffNavBar(self.window, self)
        # Connect to the database and retrieve data and fields
        self.myDB = DataBase("mydatabase.db")  
        fields = self.myDB.get_fields("USERS")  
        self.data = self.myDB.fetch_all("Users")
        # Populate the LabelFrame with fields
        self.populate(fields)
        # Add a listbox to display reservations
        self.UserList = MyListBox(self, 6, 0, "mydatabase.db", "USERS")
        # Add a CRUD button widget to allow the user to search for reservations
        self.crudButtonWidget = CRUD(self, self.UserList, "mydatabase.db", "USERS", 7, 0, ["Update"])

    # Add widgets for each field in the LabelFrame
    def populate(self, fieldNames):
        r, c = 1, 0
        for i in range(0, len(fieldNames)):
            Widget(self, r, c, fieldNames[i])
            r+=1

# Create a test window and add a screen3 LabelFrame to it
if __name__ == "__main__":
    testWindow = tk.Tk()
    testFrame = screen3(testWindow, "Account")
    testWindow.mainloop()