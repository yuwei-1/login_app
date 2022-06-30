import sqlite3


class DatabaseQueries:

    def __init__(self):

        con = sqlite3.connect("loginapp.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS login_details (Username TEXT, Password TEXT)")
        con.commit()
        con.close()

    def create_new(self, new_user, new_pw):

        con = sqlite3.connect("loginapp.db")
        cursor = con.cursor()
        cursor.execute("SELECT Password FROM login_details WHERE Username = ?", (new_user,))
        records = cursor.fetchall()

        if records:

            return True

        cursor.execute("INSERT INTO login_details (Username, Password) VALUES (?, ?)", (new_user, new_pw))
        con.commit()
        con.close()

        return False

    def check_details(self, user, pw) -> bool:

        con = sqlite3.connect("loginapp.db")
        cursor = con.cursor()
        cursor.execute("SELECT Password FROM login_details WHERE Username = ?", (user,))
        records = cursor.fetchall()
        con.commit()
        con.close()

        if records:

            if records[0][0] == pw:
                return True

        return False
