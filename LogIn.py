import tkinter as tk
import sqlite3
from tkinter import ttk
from database import *
from Label import *
from Entry import *
from basicbutton import *
import Manager.ManagerMain
import Staff.StaffMain
import Customer.CustomerMain
import sqlite3

class Login(ttk.Frame):
        def __init__(self, window, title):
                super().__init__(window)
                self.window = window
                self.title = title

                gridOptions = {'padx':5, 'pady':5, 'sticky':tk.NSEW}      
                self.grid(row = 0, column = 0, **gridOptions)

                self.myDB = DataBase("mydatabase.db")
                self.UsernameLabel = label(self, 1, 0, "Username")
                self.UsernameVar = tk.StringVar()
                self.UsernameEntry = entry(self, 1, 1, self.UsernameVar)
                self.PasswordLabel = label(self, 2, 0, "Password")
                self.PasswordVar = tk.StringVar()
                self.PasswordEntry = entry(self, 2, 1, self.PasswordVar)
                self.EntryButton = button(self, 3, 0, "Enter", lambda:Login.LogInCommand(self))
                self.CustomerButton = button(self, 3, 1, "Reserve Table Now!", lambda:Login.CustomerCommand(self))

        def LogInCommand(self):
                # get the username and password from the StringVar objects
                username = self.UsernameVar.get()
                password = self.PasswordVar.get()

                # establish a connection to the database
                conn = sqlite3.connect('mydatabase.db')

                # create a cursor object
                c = conn.cursor()

                # execute an SQL query to search for a matching username and password
                c.execute('SELECT AccessLevel FROM Users WHERE Username=? AND Password=?', (username, password))

                # fetch the results of the query
                result = c.fetchone()

                # close the database connection
                conn.close()

                # check if a matching user was found and direct them to the correct view
                if result:
                        access_level = result[0]

                        if access_level == 'Manager':
                                Manager.ManagerMain.App()
                                return
                        elif access_level == 'Staff':
                                Staff.StaffMain.App()
                                return
                
                else:
                        print('Invalid username or password.')

        def CustomerCommand(Self):
                Customer.CustomerMain.App()
                return

if __name__=="__main__":
    loginwindow = tk.Tk()
    login = Login(loginwindow, "log in")
    loginwindow.mainloop()
