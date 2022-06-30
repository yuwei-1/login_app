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
            q1 = DatabaseQueries()

            if q1.check_details(p1.user, p1.pw):
                p1.successful_login()

            else:
                p1.invalid_login()

            p1.user = None
            p1.pw = None

        if p1.newuser:

            if p1.confirmpw == p1.newpw:

                q1 = DatabaseQueries()
                exists = q1.create_new(p1.newuser, p1.newpw)

                if not exists:
                    p1.reg.destroy()
                    p1.display_message(window, "Registration was Successful")
                else:
                    p1.display_message(p1.reg, "This Account already exists")

            p1.newuser = None

        try:
            window.update_idletasks()
            window.update()

        except:
            break

