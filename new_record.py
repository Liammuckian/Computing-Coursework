import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from basic_wid import *
from database import *

class NewRecord():
    def __init__(self, parent, fields, db, table, list):
        # Set instance variables based on the arguments passed in
        self.parent = parent
        self.fields = fields
        self.db = db
        self.table = table
        self.list = list
        self.r, self.c = 0, 0
        self.window = tk.Toplevel()

        # Create a widget for each field in the specified list of fields
        for i in range(1,len(self.fields)):
            Widget(self.window,self.r, self.c, self.fields[i])
            self.r+=1

        # Create "Save" and "Close" buttons
        self.saveButton = ttk.Button(self.window, text = "Save", command = self.return_data)
        self.saveButton.grid(row=self.r, column=self.c, pady=5, padx=5)
        self.closeButton = ttk.Button(self.window, text = "Close", command=self.window.destroy)
        self.closeButton.grid(row=self.r, column=self.c+1, pady=5, padx=5)

        # Start the Tkinter event loop to display the window
        self.window.mainloop()

# Retrieve data from the input fields, add it to the database, and update the listbox
    def return_data(self):
        # Get the value of each input field
        data = [w.get() for w in self.window.winfo_children() if type(w)==ttk.Entry]
        
        # Add the data to the database
        myDB = DataBase(self.db)
        myDB.add_record(self.table, data)

        # Update the listbox with all the records from the database
        self.list.fillListBox(myDB.fetch_all(self.table))

        # Show a message box confirming that the record was added
        messagebox.showinfo("Addition", "Record added to Database")

        # Close the record form window
        self.window.destroy()


if __name__=="__main__":
    # Create a new tkinter window
    testWindow = tk.Tk()

    # Define a function to create a new record form and display it
    def test():
        # Create a new instance of the NewRecord class
        new = NewRecord(testWindow, ["Name", "Age"], None, None, None)

    # Create a button to test the NewRecord class
    testButton = ttk.Button(testWindow, text = "Test", command = lambda:test())
    testButton.grid(row = 0, column=0)

    # Start the tkinter event loop
    testWindow.mainloop()









if __name__=="__main__":
    testWindow = tk.Tk()

    def test():
        new = NewRecord(testWindow, ["Name", "Age"], None, None, None)

    testButton = ttk.Button(testWindow, text = "Test", command = lambda:test())
    testButton.grid(row = 0, column=0)

    testWindow.mainloop()
