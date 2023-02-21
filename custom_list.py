import tkinter as tk
import sqlite3
from tkinter import ttk
import os
from database import *

class MyListBox(tk.Listbox):
    def __init__(self,parent, r, c, DB, table):
        super().__init__(parent)
        self.parent = parent
        self.r = r
        self.c = c
        self.DB = DB
        self.table = table
        self.recordsList = tk.Listbox(self.parent, width = 60, height = 10)

        # Bind method to listbox select event
        self.recordsList.bind('<<ListboxSelect>>', self.onSelect)

        self.recordsList.grid(row =self.r, column = self.c, padx = 5, pady = 5, columnspan=5)

        # Connect to database and retrieve all data from the specified table
        myDb = DataBase(self.DB)
        self.data = myDb.fetch_all(self.table)

        # Fill the listbox with the data
        self.fillListBox(self.data)

    def onSelect(self, evt):
        # Clear all entry widgets
        entryWids = [w for w in self.parent.winfo_children() if type(w)==ttk.Entry]
        for w in entryWids:
            w.delete(0, tk.END)

        # Get the selected record from the listbox and insert the values into the entry widgets
        selectedRecord = self.recordsList.get(tk.ANCHOR).split(",")
        for i in range(0, len(selectedRecord)-1):
            entryWids[i].insert(0,selectedRecord[i])

    def fillListBox(self, data):
        # Clear the listbox
        self.recordsList.delete(0, tk.END)

        # Iterate through the data and add each item to the listbox
        for item in data:
            string = ''
            for word in item:
                string+=f"{str(word)},"
            self.recordsList.insert(0, string)

if __name__ =="__main__":
    # Create a test window and MyListBox object
    testwindow = tk.Tk()
    testBox = MyListBox(testwindow, 0, 0, os.path.dirname(os.getcwd())+"\\mydatabase.db", "RESERVATIONS")

    # Run the mainloop to display the window and interact with the program
    testwindow.mainloop()