from database import db
from user_functions import *
from staff_fuctions import *
from room_functions import *
from reservation import *


while True:
    select = input("""
1.user
2.staff
3.room
4.reservation
5.exit

select a option:\n""")
    
    # user
    if select == "1":
        choice = input("""
1.add
2.delete
3.update
4.show

select a option:\n""")
        
        if choice == "1":
            national_code = int(input("enter a national code: "))
            first_name = input("enter a first name: ")
            last_name = input("enter a last name: ")
            number_phone = input("enter a number phone: ")
            add_user(national_code, first_name, last_name, number_phone)
            print("user added successfully!")
            
        elif choice == "2":
            national_code = int(input("enter a national code for delet user: "))
            delet_user(national_code)
            print("user deleted successfully!")
            
        elif choice == "3":
            national_code = int(input("enter a national code for update user: "))
            new_first_name = input("enter new first name: ")
            new_last_name = input("enter new last name: ")
            new_number_phone = input("enter new number phone: ")
            update_user(national_code, new_first_name, new_last_name, new_number_phone)
            print("user updated seccessfully!")
            
        elif choice == "4":
            print()
            display_users()
        else:
            print("error")
            

    # staff
    if select == "2":
        choice = input("""
1.add
2.delete
3.update
4.show

select a option:\n""")
        
        if choice == "1":
            personal_id = int(input("enter a personal id: "))
            first_name = input("enter a first name: ")
            last_name = input("enter a last name: ")
            add_staff(personal_id, first_name, last_name)
            print("staff added successfully!")
            
        elif choice == "2":
            personal_id = int(input("enter a personal id for delet user: "))
            delet_staff(personal_id)
            print("staff deleted successfully!")
            
        elif choice == "3":
            personal_id = int(input("enter a personal id code for update staff: "))
            new_first_name = input("enter new first name: ")
            new_last_name = input("enter new last name: ")
            update_staff(personal_id, new_first_name, new_last_name)
            print("staff updated seccessfully!")
            
        elif choice == "4":
            print()
            display_staff()
        else:
            print("error")
            
    # room
    if select == "3":
        choice = input("""
1.add
2.delete
3.update
4.show

select a option:\n""")
        
        if choice == "1":
            room_id = int(input("enter a room id: "))
            price = input("enter a price: ")
            add_room(room_id, price)
            print("room added successfully!")
            
        elif choice == "2":
            room_id = int(input("enter a room id for delete: "))
            delet_room(room_id)
            print("room deleted successfully!")
            
        elif choice == "3":
            room_id = int(input("enter a room id for update: "))
            new_price = input("enter new price: ")
            update_room(room_id, new_price)
            print("room updated seccessfully!")
            
        elif choice == "4":
            print()
            display_room()
        else:
            print("error")
            
            
    # reserve
    if select == "4":
        choice = input("""
1.add new reserve
2.delete reserve
3.update resserve
4.show reserve

select a option:\n""")
        
        if choice == "1":
            room_id = int(input("enter a room id: "))
            user_national_code = int(input("enter a user national code: "))
            staff_personal_id = int(input("enter a staff personal id: "))
            add_reserve(room_id, user_national_code, staff_personal_id)
            print("reservation added successfully!")
            
        elif choice == "2":
            room_id = int(input("enter a room id for delete: "))
            delet_reserve(room_id)
            print("reservation deleted successfully!")
            
        elif choice == "3":
            room_id = int(input("enter a room id for update: "))
            national_code = int(input("enter a national code for update reservation: "))
            update_reserve(room_id, national_code)
            print("room updated seccessfully!")
            
        elif choice == "4":
            print()
            display_reserve()
        else:
            print("error")
    if select == "5":
        print("good luck")
        break