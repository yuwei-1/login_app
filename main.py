from display import LoginPage
import sqlite3
from tkinter import *
from tkinter.ttk import *

if __name__ == "__main__":

    window = Tk()

    p1 = LoginPage("Login page", window, "Login")
    p1.create_page()

    while True:

        if p1.user:
            print(p1.user)
            p1.user = None

        window.update_idletasks()
        window.update()
