from database import db

def add_staff(personal_id, first_name, last_name):
    with db.connect:
        db.cursor.execute("""INSERT INTO staff(personal_id, first_name, last_name) VALUES
                     (:personal_id, :first_name, :last_name)""",
                      {
                          'personal_id': personal_id, 
                          'first_name': first_name,
                          'last_name': last_name
                      })


def delet_staff(personal_id):
    with db.connect:
        db.cursor.execute("""DELETE FROM staff WHERE personal_id=(:personal_id)""",
                                {'personal_id': personal_id})
        
def update_staff(personal_id, first_name, last_name):
    with db.connect:
        db.cursor.execute("""UPDATE sfaff 
                            SET first_name = :first_name, 
                                last_name = :last_name, 
                                WHERE personal_id = :personal_id""",
                          {'first_name': first_name, 'last_name': last_name, 'personal_id': personal_id}
                      )

def display_staff():
    with db.connect:
        db.cursor.execute("SELECT personal_id, first_name, last_name FROM staff")
        staffs = db.cursor.fetchall()

        if not staffs:
            print("not found staff")
            return

        print("{:<15} {:<15} {:<15}".format("personal id", "firstname", "lastname"))
        print("-" * 60)

        for staff in staffs:
            print("{:<15} {:<15} {:<15}".format(staff[0], staff[1], staff[2]))

