import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


class LoginPage:

    def __init__(self, title, window,  button=None):
        self.title = title
        self.button = button
        self.window = window
        self.user = None
        self.pw = None
        self.email = None
        self.new_user = None
        self.new_pw = None
        self.confirm_pw = None
        self.reg = None
        self.code = None
        self.auth = None

    def create_login_page(self):

        self.window.title("Login")
        self.window.geometry("500x500+500+200")

        self.create_label(self.window, self.title, 30)
        username = self.create_field(self.window, "Username:", 0.4, 15)
        password = self.create_field(self.window, "Password:", 0.5, 15)

        self.create_button(self.window, lambda: self.get_login_details(username, password))
        self.create_register(self.window)

    def create_register(self, window):

        style = Style()
        style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='red')

        label = Label(window, text="Not a user?", font=("calibri", 10))
        label.place(relx=0.5, rely=0.57, anchor=E)

        e = tk.Button(window, text="Register", command=lambda: self.register(), borderwidth=0, highlightthickness=0, font=('calibri', 10, 'bold', 'underline'), foreground='blue')
        e.place(relx=0.5, rely=0.57, anchor=W)

    def create_email_authenticator(self):

        authenticator = Toplevel(self.window)
        self.auth = authenticator

        authenticator.geometry("400x400+550+250")
        authenticator.title("Email Authenticator")
        self.create_label(authenticator, "A 6-Digit code has been sent\nto the email you used for registration.", 10)
        code = self.create_field(authenticator, "Code:", 0.4, 15)
        Button(authenticator, text="Verify",
               command=lambda: self.get_code(code)).place(relx=0.5, rely=0.75, anchor=CENTER)

    def get_login_details(self, username, password):

        self.user = username.get()
        self.pw = password.get()

    def get_code(self, code):

        self.code = code.get()

    def get_new_login(self, new_user, new_pw, confirm_pw, email):

        self.new_user = new_user.get()
        self.new_pw = new_pw.get()
        self.confirm_pw = confirm_pw.get()
        self.email = email.get()

    def register(self):

        reg = Toplevel(self.window)

        self.reg = reg
        reg.geometry("500x500+500+200")
        reg.title("Register Page")
        self.create_label(reg, "Register", 30)

        new_user = self.create_field(reg, "New username: ", 0.27, 10)
        new_pass = self.create_field(reg, "New password: ", 0.34, 10)
        confirm_new_pass = self.create_field(reg, "Confirm password: ", 0.41, 10)
        email_address = self.create_field(reg, "Email address: ", 0.48, 10)

        Button(reg, text="Back", command=lambda: reg.destroy()).place(relx=0.5, rely=0.75, anchor=CENTER)
        Button(reg, text="Register", command=lambda: self.get_new_login(
            new_user, new_pass, confirm_new_pass, email_address)).place(relx=0.5, rely=0.65, anchor=CENTER)

    @staticmethod
    def create_label(win, title, text_size):
        l1 = tk.Label(win, text=title, font=("calibri", text_size), borderwidth=1, highlightthickness=1, relief='solid', background='white')
        l1.place(relx=0.5, rely=0.1, anchor=CENTER)

    def create_button(self, win, command):

        b = Button(win, text=self.button, width=20, command=command)
        b.place(relx=0.5, rely=0.75, anchor=CENTER)

    @staticmethod
    def create_field(win, name, y_pos, text_size):

        label = Label(win, text=name, font=("calibri", text_size))
        label.place(relx=0.495, rely=y_pos, anchor=E)

        if "password" in name.lower():
            e = Entry(win, show="●")
        else:
            e = Entry(win)
        e.place(relx=0.505, rely=y_pos, anchor=W)
        return e

    @staticmethod
    def display_message(win, msg):

        l2 = Label(win, text=msg)
        l2.place(relx=0.35, rely=0.55)


class LandingPage(LoginPage):

    def __init__(self, window, user, email):

        self.window = window
        self.user = user
        self.email = email
        self.img = ImageTk.PhotoImage(file="Images/fsocietywallpaper.png")

    def create_landing_page(self):

        self.window.configure(bg='black')
        self.window.title("Landing Page")
        self.window.geometry("1350x700+0+50")

        label = tk.Label(image=self.img, borderwidth=0, highlightthickness=0)
        label.place(relx=0.5, rely=0.6, anchor=CENTER)

        super().create_label(self.window, "Welcome, " + self.user, 30)

        self.display_user_data()

    def display_user_data(self):

        l1 = Label(self.window, text=self.user, font=("Times 20 italic bold", 10))
        l2 = Label(self.window, text=self.email, font=("Times 20 italic bold", 10))

        l1.place(relx=0.85, rely=0)
        l2.place(relx=0.85, rely=0.03)
