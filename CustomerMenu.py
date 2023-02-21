import tkinter as tk
from tkinter import ttk
from Customer.CustomerNav import CustomerNavBar
from database import *
from basic_wid import *
from custom_list import *
from crud import *
from Label import *


# Define the screen3 class that inherits from ttk.LabelFrame
class screen3(ttk.LabelFrame):
    # Initialize the screen3 class
    def __init__(self, window, title):
        # Call the __init__ method of the parent class ttk.LabelFrame
        super().__init__(window)
        self.window = window
        self.title = title
        self['text'] = self.title
        
        # Set the grid options for the frame
        gridOptions = {'padx': 5, 'pady': 5, 'sticky': tk.NSEW}
        self.grid(row=0, column=0, **gridOptions)
        
        # Create a navigation bar and a database object
        self.navigation = CustomerNavBar(self.window, self)
        self.myDB = DataBase("mydatabase.db")  
        
        # Get the field names and data from the database and populate the frame
        fields = self.myDB.get_fields("MENU")  
        self.data = self.myDB.fetch_all("Menu")
        self.populate(fields)
        
        # Create a listbox and a CRUD button widget
        self.ReviewList = MyListBox(self, 6, 0, "mydatabase.db", "MENU")
        self.crudButtonWidget = CRUD(self, self.ReviewList, "mydatabase.db", "MENU", 7, 0, [])
    
    # Method to populate the frame with widgets for each field
    def populate(self, fieldNames):
        r, c = 1, 0
        for i in range(0, len(fieldNames)):
            Widget(self, r, c, fieldNames[i])
            r += 1

# If the script is being run directly, create a test instance of the screen3 class and start the Tkinter main event loop
if __name__ == "__main__":
    testWindow = tk.Tk()
    testFrame = screen3(testWindow, "Menu")
    testWindow.mainloop()