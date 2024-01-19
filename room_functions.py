from database import db

def add_room(room_id, price):
    with db.connect:
        db.cursor.execute("""INSERT INTO room(room_id, price, status) VALUES
                     (:room_id, :price, :status)""",
                      {
                          'room_id': room_id, 
                          'price': price,
                          'status': False
                      })


def delet_room(room_id):
    with db.connect:
        db.cursor.execute("""DELETE FROM room WHERE room_id=(:room_id)""",
                                {'room_id': room_id})
        
def update_room(room_id, price):
    with db.connect:
        db.cursor.execute("""UPDATE room 
                            SET price = :price 
                            WHERE room_id = :room_id""",
                          {'price': price, 'room_id': room_id}
                      )

def display_room():
    with db.connect:
        db.cursor.execute("SELECT room_id, price, status FROM room")
        rooms = db.cursor.fetchall()

        if not rooms:
            print("not found room")
            return

        print("{:<15} {:<15} {:<15}".format("room_id", "price", "status"))
        print("-" * 60)

        for room in rooms:
            print("{:<15} {:<15} {:<15}".format(room[0], room[1], room[2]))
