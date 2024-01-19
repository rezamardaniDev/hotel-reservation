from database import db

def add_user(national_code, first_name, last_name, number_phone):
    with db.connect:
        db.cursor.execute("""INSERT INTO users(national_code, first_name, last_name, number_phone) VALUES
                     (:national_code, :first_name, :last_name, :number_phone)""",
                      {
                          'national_code': national_code, 
                          'first_name': first_name,
                          'last_name': last_name,
                          'number_phone': number_phone
                      })


def delet_user(national_code):
    with db.connect:
        db.cursor.execute("""DELETE FROM users WHERE national_code=(:national_code)""",
                                {'national_code': national_code})
        
def update_user(national_code, first_name, last_name, phone_number):
    with db.connect:
        db.cursor.execute("""UPDATE users 
                            SET first_name = :first_name, 
                                last_name = :last_name, 
                                number_phone = :phone_number 
                                WHERE national_code = :national_code""",
                          {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_number, 'national_code': national_code}
                      )

def display_users():
    with db.connect:
        db.cursor.execute("SELECT national_code, first_name, last_name, number_phone FROM users")
        users = db.cursor.fetchall()

        if not users:
            print("not found user")
            return

        print("{:<15} {:<15} {:<15} {:<15}".format("national code", "firstname", "lastname", "phone"))
        print("-" * 60)

        for user in users:
            print("{:<15} {:<15} {:<15} {:<15}".format(user[0], user[1], user[2], user[3]))
