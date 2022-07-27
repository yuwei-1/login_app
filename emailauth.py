import smtplib
import ssl
import random


class EmailHandler:

    def __init__(self, receiver_email=None):

        self.port = 465
        self.app_pw = "hjxscnoklbkmjowg"
        self.context = ssl.create_default_context()
        self.receiver_email = receiver_email
        self.sender_email = "loginappnoreply@gmail.com"
        self.code = None

    def send_email(self):

        text = "Hi User,\n\nYou have successfully registered an account with LoginApp. " \
               "This email was sent by Python. \n\nKind regards,\nLogin App Team"
        subject = "Successful Registration"
        message = 'Subject: {}\n\n{}'.format(subject, text)

        try:

            with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
                server.login(self.sender_email, self.app_pw)
                server.sendmail(self.sender_email, self.receiver_email, message)

                return True

        except smtplib.SMTPRecipientsRefused:

            return False

    def send_verification_code(self):

        self.code = self.create_code()

        text = "Hi User,\n\nPlease see verification code for login: " \
               "{}".format(self.code) + "\nDo not share this code with anyone else."
        subject = "Login Verification Code"
        message = 'Subject: {}\n\n{}'.format(subject, text)

        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.sender_email, self.app_pw)
            server.sendmail(self.sender_email, self.receiver_email, message)

    @staticmethod
    def create_code():

        code = ""

        for i in range(6):
            code += str(random.randint(0, 9))

        return code
