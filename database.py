import sqlite3

class Connector:
    def __init__(self):
        self.connect = sqlite3.connect('myDatabase.db')
        self.cursor = self.connect.cursor()
        self.create_table_user()
        self.create_table_staff()
        self.create_table_room()
        self.create_table_reservation()
        
    def create_table_user(self):
        with self.connect:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                national_code INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                number_phone TEXT
            )""")
            
    def create_table_staff(self):
        with self.connect:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS staff(
                personal_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            )""")
            
    def create_table_room(self):
        with self.connect:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS room(
                room_id INTEGER PRIMARY KEY,
                price TEXT,
                status boolean
            )""")
            
    def create_table_reservation(self):
        with self.connect:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS reservation(
                user_national_code INTEGER,
                staff_personal_id INTEGER,
                room_id INTEGER,
                FOREIGN KEY (user_national_code) REFERENCES users(national_code),
                FOREIGN KEY (staff_personal_id) REFERENCES staff(personal_id),
                FOREIGN KEY (room_id) REFERENCES room(room_id)
            )""")


db = Connector()
if __name__ == "__main__":
    print("Database connection setup seccessfully")