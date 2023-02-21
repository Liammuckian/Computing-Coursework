import tkinter as tk
from tkinter import ttk
from database import *
import os
from custom_list import *
from new_record import *
from tkinter import messagebox

class CRUD():
    def __init__(self, parent, listbox, DB, table, r, c, permissions):
        # Initialize the CRUD class with the necessary parameters
        self.parent = parent
        self.listbox = listbox
        self.DB = DB
        self.table = table
        self.r = r
        self.c = c
        self.permissions = permissions
        gridOptions = {'padx':5, 'pady':5}
        
        # Create a frame to hold the buttons and widgets
        self.holdingFrame=ttk.Frame(self.parent)
        self.holdingFrame.grid(row = self.r, column=self.c, columnspan= 7, padx=5, pady=5)
        
        # Create a search entry and button
        self.searchVar = tk.StringVar()
        self.searchEntry = tk.Entry(self.holdingFrame, textvariable=self.searchVar)
        self.searchEntry.grid(row = self.r, column=self.c, **gridOptions)
        self.buttonNames = ["Search"]
        
        # Add Update, Delete, and New buttons if the user has permission
        if 'Update' in permissions:
            self.buttonNames.append("Update")
        if 'Delete' in permissions:
            self.buttonNames.append("Delete")
        if 'New' in permissions:
            self.buttonNames.append("New")
        
        # Create the buttons and add them to the frame
        self.c+=1
        for b in self.buttonNames:
            button = ttk.Button(self.holdingFrame,  text = b,command=lambda x=b:self.operations(x))
            button.grid(row=self.r, column=self.c, **gridOptions )
            self.c+=1

    def operations(self, op):
        # Get the data from the parent widgets
        data = [w.get() for w in self.parent.winfo_children() if type(w)==ttk.Entry]
        
        # Search the database based on the search criteria
        if op == "Search":
            criteria = self.searchVar.get()
            myDB = DataBase(self.DB)
            fields = myDB.get_fields(self.table)
            results = myDB.getData(self.table, fields[2], criteria)
            self.listbox.fillListBox(results)
        
        # Update the selected record in the database
        if op == "Update" and 'Update' in self.permissions:
            myDB = DataBase(self.DB)
            fields = myDB.get_fields(self.table)
            for i in range(0, len(data)):
                myDB.update_data(self.table,fields[i],data[i], fields[0], data[0])
            self.listbox.fillListBox(myDB.fetch_all(self.table))
            messagebox.showinfo("Update", "Record updated successfuly")
        
        # Delete the selected record from the database
        if op == "Delete" and 'Delete' in self.permissions:
            myDB = DataBase(self.DB)
            fields = myDB.get_fields(self.table)
            myDB.delete_record(fields[0],self.table,data[0])
            self.listbox.fillListBox(myDB.fetch_all(self.table))
            messagebox.showinfo("Deletion", "Record deleted")
        
        # Open a new window to create a new record in the database
        if op == "New" and 'New' in self.permissions:
            myDB = DataBase(self.DB)
            fields = myDB.get_fields(self.table)
            myDB.close()
            new = NewRecord(self.parent, fields,self.DB, self.table, self.listbox)