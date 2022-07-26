import smtplib, ssl
import random

class EmailHandler:

    def __init__(self, receiver_email = None):

        self.port = 465
        self.app_pw = "hjxscnoklbkmjowg"
        self.context = ssl.create_default_context()
        self.receiver_email = receiver_email
        self.sender_email = "loginappnoreply@gmail.com"
        self.code = None

    def send_email(self):

        TEXT = "Hi User,\n\nYou have successfully registered an account with LoginApp. " \
               "This email was sent by Python. \n\nKind regards,\nYuwei"
        SUBJECT = "Successful Registration"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        try:

            with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
                server.login(self.sender_email, self.app_pw)
                server.sendmail(self.sender_email, self.receiver_email, message)

                return True

        except:

            return False

    def send_verification_code(self):

        self.code = self.create_code()

        TEXT = "Hi User,\n\nPlease see verification code for login: " \
               "{}".format(self.code) + "\nDo not share this code with anyone else."
        SUBJECT = "Login Verification Code"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.sender_email, self.app_pw)
            server.sendmail(self.sender_email, self.receiver_email, message)

    @staticmethod
    def create_code():

        code = ""

        for i in range(6):
            code += str(random.randint(0, 9))

        return code








