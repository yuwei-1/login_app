from display import LoginPage
import sqlite3
from tkinter import *
from tkinter.ttk import *
from queries import DatabaseQueries

if __name__ == "__main__":

    window = Tk()

    p1 = LoginPage("Login page", window, "Login")
    p1.create_page()

    while True:

        if p1.user:
            print(p1.user)
            print(p1.pw)

            q1 = DatabaseQueries()
            if q1.check_details(p1.user, p1.pw):

                print("Login Successful")

            else:

                print("Invalid Login")

            p1.user = None
            p1.pw = None

        if p1.newuser:

            if p1.confirmpw == p1.newpw:

                q1 = DatabaseQueries()
                q1.create_new(p1.newuser, p1.newpw)

            p1.newuser = None

        window.update_idletasks()
        window.update()
