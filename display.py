import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk


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
        username = self.create_field(self.window, "Username:", 0.43, 0.4, 10)
        password = self.create_field(self.window, "Password:", 0.43, 0.5, 10)

        self.create_button(self.window, lambda: self.get_login_details(username, password))
        self.create_register(self.window)

    def create_register(self, window):

        frame = tk.Frame(window)

        label = Label(frame, text="Not a user?", font=("helvetica", 8))
        label.grid(column=0, row=0)

        e = tk.Button(frame, text="Register", command=lambda: self.register(), borderwidth=0,
                      highlightthickness=0, font=('helvetica', 8, 'underline'), foreground='blue')
        e.grid(column=1, row=0)

        frame.place(relx=0.295, rely=0.55, anchor=NW)

    def create_email_authenticator(self):

        authenticator = Toplevel(self.window)
        self.auth = authenticator

        authenticator.geometry("400x400+550+250")
        authenticator.title("Email Authenticator")
        self.create_label(authenticator, "A 6-Digit code has been sent\nto the email you used for registration.", 10)
        code = self.create_field(authenticator, "Code:", 0.4, 0.4, 10)
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

        new_user = self.create_field(reg, "New username: ", 0.5, 0.27, 10)
        new_pass = self.create_field(reg, "New password: ", 0.5, 0.34, 10)
        confirm_new_pass = self.create_field(reg, "Confirm password: ", 0.5, 0.41, 10)
        email_address = self.create_field(reg, "Email address: ", 0.5, 0.48, 10)

        b1 = Button(reg, text="Back", command=lambda: reg.destroy())
        b2 = Button(reg, text="Register", command=lambda: self.get_new_login(
            new_user, new_pass, confirm_new_pass, email_address))

        b1.place(relx=0.5, rely=0.8, anchor=CENTER)
        b2.place(relx=0.5, rely=0.7, anchor=CENTER)

    @staticmethod
    def create_label(win, title, text_size):
        l1 = tk.Label(win, text=title, font=("helvetica", text_size),
                      borderwidth=1, highlightthickness=1, relief='solid', background='black', foreground='white')
        l1.place(relx=0.5, rely=0.1, anchor=CENTER)

    def create_button(self, win, command):

        b = Button(win, text=self.button, width=20, command=command)
        b.place(relx=0.5, rely=0.75, anchor=CENTER)

    @staticmethod
    def create_field(win, name, x_pos, y_pos, text_size):

        label = Label(win, text=name, font=("helvetica", text_size))
        label.place(relx=x_pos - 0.005, rely=y_pos, anchor=E)

        if "password" in name.lower():
            e = tk.Entry(win, show="●", borderwidth=1, relief='solid')
        else:
            e = tk.Entry(win, borderwidth=1, relief='solid')

        e.place(relx=x_pos + 0.005, rely=y_pos, anchor=W)
        return e

    @staticmethod
    def display_message(win, msg):

        frame = tk.Frame(win)
        l2 = tk.Label(frame, text=msg, width = 200)
        l2.grid(column=0, row=0)

        frame.place(relx=0.5, rely=0.63, anchor=CENTER)

    @staticmethod
    def check_password(pw):

        if len(pw) < 8:
            return False
        if pw.lower() == pw:
            return False
        if not any(not s.isalnum() for s in pw):
            return False
        return True


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

        l1 = Label(self.window, text=self.user, font=("helvetica", 10))
        l2 = Label(self.window, text=self.email, font=("helvetica", 10))

        l1.place(relx=0.85, rely=0)
        l2.place(relx=0.85, rely=0.03)
