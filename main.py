from display import LoginPage
from tkinter import *
from queries import DatabaseQueries
from emailauth import EmailHandler


if __name__ == "__main__":

    window = Tk()

    p1 = LoginPage("Login page", window, "Login")
    p1.create_page()

    while True:

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
                        else:
                            p1.display_message(window, "Your code is incorrect.")

                        p1.auth.destroy()
                        p1.code = None
                        break

                    try:
                        p1.auth.update_idletasks()
                        p1.auth.update()
                    except:
                        break

            else:
                p1.display_message(window, "         Invalid Login")

            p1.user = None
            p1.pw = None

        if p1.newuser:

            e1 = EmailHandler(receiver_email = p1.email)

            if p1.confirmpw == p1.newpw:

                q1 = DatabaseQueries()
                exists = q1.check_new(p1.newuser, p1.email)

                if not exists:

                    if e1.send_email():
                        q1.create_new(p1.newuser, p1.newpw, p1.email)
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


            p1.newuser = None

        try:
            window.update_idletasks()
            window.update()

        except:

            break

