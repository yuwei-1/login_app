from tkinter import *
from tkinter.ttk import *

class loginpage():

    def __init__(self, title, button=None):
        self.title = title
        self.button = button

    def create_page(self):

        window = Tk()
        window.title("Login")
        window.geometry("500x500+500+200")
        self.window = window

        self.create_label(window, self.title)
        self.create_button(window, lambda: self.invalid_login())
        self.create_field(window, "Username:", 0.25)
        self.create_field(window, "Password:", 0.35)

        window.mainloop()


    def invalid_login(self):

        err = Toplevel(self.window)
        err.geometry("100x100+700+400")
        err.title("Login Error")
        Label(err, text = "Invalid Login").place(relx=0.5, rely=0.5, anchor=CENTER)
        Button(err, text = "ok", command = err.destroy).place(relx=0.5, rely=0.75, anchor = CENTER)


    def create_label(self, win, title):

        l1 = Label(win, text=title, font=("Times 20 italic bold", 20))
        l1.pack()

    def create_button(self, win, command):

        b = Button(win, text = self.button, width = 20, command = command)
        b.place(relx=0.5, rely=0.75, anchor=CENTER)

    def create_field(self, win, name, ypos):

        label = Label(win, text = name, font=("Times 20 italic bold", 15))
        label.place(relx=0.25, rely=ypos)

        e = Entry(win)
        e.place(relx=0.5, rely=ypos)



p1 = loginpage("Login page", "Login")

p1.create_page()