from database import db

def add_reserve(room_id, user_national_code, staff_personal_id):
    with db.connect:
        db.cursor.execute("""INSERT INTO reservation(user_national_code, staff_personal_id, room_id) VALUES
                     (:user_national_code, :staff_personal_id, :room_id)""",
                      {
                          'user_national_code': user_national_code, 
                          'staff_personal_id': staff_personal_id,
                          'room_id': room_id
                      })
        db.cursor.execute("""UPDATE room 
                            SET status = :status 
                            WHERE room_id = :room_id""",
                          {'status': True, 'room_id': room_id}
                      )


def delet_reserve(room_id):
    with db.connect:
        db.cursor.execute("""DELETE FROM reservation WHERE room_id=(:room_id)""",
                                {'room_id': room_id})
        
def update_reserve(room_id, user_national_code):
    with db.connect:
        db.cursor.execute("""UPDATE reservation 
                            SET user_national_code = :user_national_code 
                            WHERE room_id = :room_id""",
                          {'user_national_code': user_national_code, 'room_id': room_id}
                      )

def display_reserve():
    with db.connect:
        db.cursor.execute("SELECT user_national_code, user_national_code, room_id status FROM reservation")
        rooms = db.cursor.fetchall()

        if not rooms:
            print("not found room")
            return

        print("{:<15} {:<15} {:<15}".format("user", "staff", "room id"))
        print("-" * 60)

        for room in rooms:
            print("{:<15} {:<15} {:<15}".format(room[0], room[1], room[2]))
