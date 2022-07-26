from tkinter import *
from tkinter.ttk import *


class LoginPage:

    def __init__(self, title, window,  button = None, user = None, pw = None, email = None, newuser = None, newpw = None, reg = None):
        self.title = title
        self.button = button
        self.window = window
        self.user = user
        self.pw = pw
        self.email = email
        self.newuser = newuser
        self.newpw = newpw
        self.reg = reg
        self.code = None
        self.auth = None

    def create_page(self):

        self.window.title("Login")
        self.window.geometry("500x500+500+200")

        self.create_label(self.window, self.title)
        username = self.create_field(self.window, "Username:", 0.25, 15)
        password = self.create_field(self.window, "Password:", 0.35, 15)

        self.create_button(self.window, lambda: self.get_login_details(username, password))
        self.create_register(self.window)

    def create_register(self, window):

        style = Style()
        style.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground='red')

        label = Label(window, text = "Not a user?", font=("Times 20 italic bold", 10))
        label.place(relx=0.3, rely=0.45)

        e = Button(window, text = "Register", style = "W.TButton", command = lambda: self.register())
        e.place(relx=0.5, rely=0.44)

    def create_email_authenticator(self):

        authenticator = Toplevel(self.window)
        self.auth = authenticator

        authenticator.geometry("400x400+550+250")
        authenticator.title("Email Authenticator")
        self.create_label(authenticator, "A 6-Digit code has been sent\nto the email you used for registration.")
        code = self.create_field(authenticator, "Code:", 0.4, 15)
        Button(authenticator, text = "Verify", command = lambda: self.get_code(code)).place(relx=0.5, rely=0.75, anchor = CENTER)

    def get_login_details(self, username, password):

        self.user = username.get()
        self.pw = password.get()

    def get_code(self, code):

        self.code = code.get()

    def get_new_login(self, newuser, newpw, confirmpw, email):

        self.newuser = newuser.get()
        self.newpw = newpw.get()
        self.confirmpw = confirmpw.get()
        self.email = email.get()

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

        new_user = self.create_field(reg, "new username: ", 0.27, 10)
        new_pass = self.create_field(reg, "new password: ", 0.34, 10)
        confirm_new_pass = self.create_field(reg, "confirm password: ", 0.41, 10)
        emailaddress = self.create_field(reg, "email address: ", 0.48, 10)

        Button(reg, text="Back", command=lambda: reg.destroy()).place(relx=0.5, rely=0.75, anchor=CENTER)
        Button(reg, text="Register", command=lambda: self.get_new_login(new_user, new_pass, confirm_new_pass, emailaddress)).place(relx=0.5, rely=0.65, anchor=CENTER)

    def create_label(self, win, title):

        l1 = Label(win, text=title, font=("Times 20 italic bold", 14))
        l1.pack()

    def create_button(self, win, command):

        b = Button(win, text = self.button, width = 20, command = command)
        b.place(relx=0.5, rely=0.75, anchor=CENTER)

    def create_field(self, win, name, ypos, textsize):

        label = Label(win, text = name, font=("Times 20 italic bold", textsize))
        label.place(relx=0.25, rely=ypos)

        if "password" in name.lower():
            e = Entry(win, show = "●")
        else:
            e = Entry(win)

        e.place(relx=0.5, rely=ypos)

        return e

    def display_message(self, win, msg):

        l2 = Label(win, text = msg)
        l2.place(relx = 0.35, rely=0.55)