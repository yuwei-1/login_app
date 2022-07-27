from display import LoginPage, LandingPage
from tkinter import *
from queries import DatabaseQueries
from emailauth import EmailHandler


if __name__ == "__main__":

    login_success = False

    window = Tk()

    p1 = LoginPage("Login page", window, "Login")
    p1.create_login_page()

    while True:

        if login_success:

            window.destroy()
            window = Tk()

            user, email = login_success
            p2 = LandingPage(window, user, email)
            p2.create_landing_page()

            login_success = False

        if p1.user:
            q1 = DatabaseQueries()
            receiver_email = q1.check_details(p1.user, p1.pw)

            if receiver_email:

                e1 = EmailHandler(receiver_email=receiver_email)
                e1.send_verification_code()
                correct_code = e1.code

                p1.create_email_authenticator()

                while True:

                    if p1.code:

                        if p1.code == correct_code:
                            p1.successful_login()
                            login_success = (p1.user, receiver_email)
                        else:
                            p1.display_message(window, "Your code is incorrect.")

                        p1.auth.destroy()
                        p1.code = None
                        break

                    try:
                        p1.auth.protocol("WM_DELETE_WINDOW", lambda: p1.auth.destroy())
                        p1.auth.update_idletasks()
                        p1.auth.update()
                    except TclError:
                        break

            else:
                p1.display_message(window, "         Invalid Login")

            p1.user = None
            p1.pw = None

        if p1.new_user:

            e1 = EmailHandler(receiver_email=p1.email)

            if p1.confirm_pw == p1.new_pw:

                q1 = DatabaseQueries()
                exists = q1.check_new(p1.new_user, p1.email)

                if not exists:

                    if e1.send_email():
                        q1.create_new(p1.new_user, p1.new_pw, p1.email)
                        p1.reg.destroy()
                        p1.display_message(window, "Registration was Successful")
                    else:
                        p1.display_message(p1.reg, "Invalid email address")

                elif exists == 1:
                    p1.display_message(p1.reg, "This Username already exists")
                elif exists == 2:
                    p1.display_message(p1.reg, "This email already exists")

            else:

                p1.display_message(p1.reg, "The passwords do not match")

            p1.new_user = None

        try:
            window.update_idletasks()
            window.update()
        except TclError:
            break
