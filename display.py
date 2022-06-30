from tkinter import *
from tkinter.ttk import *


class LoginPage:

    def __init__(self, title, window,  button = None, user = None, pw = None, newuser = None, newpw = None, reg = None):
        self.title = title
        self.button = button
        self.window = window
        self.user = user
        self.pw = pw
        self.newuser = newuser
        self.newpw = newpw
        self.reg = reg

    def create_page(self):

        self.window.title("Login")
        self.window.geometry("500x500+500+200")

        self.create_label(self.window, self.title)
        username = self.create_field(self.window, "Username:", 0.25, 15)
        password = self.create_field(self.window, "Password:", 0.35, 15)
        self.create_button(self.window, lambda: self.get_login_details(username, password))

        style = Style()
        style.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground='red')

        label = Label(self.window, text = "Not a user?", font=("Times 20 italic bold", 10))
        label.place(relx=0.25, rely=0.45)

        e = Button(self.window, text = "Register", style = "W.TButton", command = lambda: self.register())
        e.place(relx=0.42, rely=0.45)

    def get_login_details(self, username, password):

        self.user = username.get()
        self.pw = password.get()

    def get_new_login(self, newuser, newpw, confirmpw):

        self.newuser = newuser.get()
        self.newpw = newpw.get()
        self.confirmpw = confirmpw.get()

    def invalid_login(self):

        err = Toplevel(self.window)
        err.geometry("200x200+700+400")
        err.title("Login Error")
        self.create_label(err, "Invalid Login")
        Button(err, text = "ok", command = err.destroy).place(relx=0.5, rely=0.75, anchor = CENTER)

    def successful_login(self):

        success = Toplevel(self.window)
        success.geometry("200x200+700+400")
        success.title("Login Successful")
        self.create_label(success, "Login Successful")
        Button(success, text = "ok", command = success.destroy).place(relx=0.5, rely=0.75, anchor = CENTER)

    def register(self):

        reg = Toplevel(self.window)

        self.reg = reg
        reg.geometry("500x500+500+200")
        reg.title("Register Page")
        self.create_label(reg, "Register")
        new_user = self.create_field(reg, "new username: ", 0.25, 10)
        new_pass = self.create_field(reg, "new password: ", 0.35, 10)
        confirm_new_pass = self.create_field(reg, "confirm password: ", 0.45, 10)
        Button(reg, text="Back", command=lambda: reg.destroy()).place(relx=0.5, rely=0.75, anchor=CENTER)
        Button(reg, text="Register", command=lambda: self.get_new_login(new_user, new_pass, confirm_new_pass)).place(relx=0.5, rely=0.65, anchor=CENTER)

    def create_label(self, win, title):

        l1 = Label(win, text=title, font=("Times 20 italic bold", 16))
        l1.pack()

    def create_button(self, win, command):

        b = Button(win, text = self.button, width = 20, command = command)
        b.place(relx=0.5, rely=0.75, anchor=CENTER)

    def create_field(self, win, name, ypos, textsize):

        label = Label(win, text = name, font=("Times 20 italic bold", textsize))
        label.place(relx=0.25, rely=ypos)

        if "password" in name.lower():
            e = Entry(win, show = "*")
        else:
            e = Entry(win)

        e.place(relx=0.5, rely=ypos)

        return e

    def display_message(self, win, msg):

        l2 = Label(win, text = msg)
        l2.place(relx = 0.35, rely=0.55)
