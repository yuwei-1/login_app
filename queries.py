import sqlite3


class DatabaseQueries:

    def __init__(self):

        con = sqlite3.connect("loginapp.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS login_details (Username TEXT, Password TEXT, Email TEXT)")
        con.commit()
        con.close()

    def check_new(self, new_user, new_email):

        con = sqlite3.connect("loginapp.db")
        cursor = con.cursor()
        cursor.execute("SELECT Password FROM login_details WHERE Username = ?", (new_user,))
        user_records = cursor.fetchall()

        cursor.execute("SELECT Password FROM login_details WHERE Email = ?", (new_email,))
        email_records = cursor.fetchall()

        if user_records:
            return 1
        if email_records:
            return 2

        return False

    def create_new(self, new_user, new_pw, new_email):

        con = sqlite3.connect("loginapp.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO login_details (Username, Password, Email) VALUES (?, ?, ?)", (new_user, new_pw, new_email))
        con.commit()
        con.close()

    def check_details(self, user, pw) -> bool:

        con = sqlite3.connect("loginapp.db")
        cursor = con.cursor()

        cursor.execute("SELECT Password FROM login_details WHERE Username = ?", (user,))
        pw_records = cursor.fetchall()
        cursor.execute("SELECT Email FROM login_details WHERE Username = ?", (user,))
        email_records = cursor.fetchall()

        con.commit()
        con.close()

        if pw_records:

            if pw_records[0][0] == pw:
                return email_records

        return False
