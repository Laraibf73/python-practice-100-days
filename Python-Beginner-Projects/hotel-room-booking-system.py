'''Hotel Room Booking System

Features:

Display available rooms
Book room
Cancel booking
Show booking status'''

def display_available_rooms(rooms):
    print("--------Available Rooms--------")
    for room_number, room_info in rooms.items():
        if not room_info['booked']:
            print(f"Room Number: {room_number}, Type: {room_info['type']}, Price: ${room_info['price']:.2f}")
    print("-------------------------------\n")

def book_room(rooms):
    room_number = input("Enter room number to book: ")
    if room_number in rooms and not rooms[room_number]['booked']:
        rooms[room_number]['booked'] = True
        print(f"Room {room_number} has been successfully booked.\n")
    else:
        print(f"Room {room_number} is either not available or already booked.\n")

def cancel_booking(rooms):
    room_number = input("Enter room number to cancel booking: ")
    if room_number in rooms and rooms[room_number]['booked']:
        rooms[room_number]['booked'] = False
        print(f"Booking for room {room_number} has been successfully canceled.\n")
    else:
        print(f"Room {room_number} is either not booked or does not exist.\n")

def show_booking_status(rooms):
    print("--------Booking Status--------")
    for room_number, room_info in rooms.items():
        status = "Booked" if room_info['booked'] else "Available"
        print(f"Room Number: {room_number}, Type: {room_info['type']}, Price: ${room_info['price']:.2f}, Status: {status}")
    print("-------------------------------\n")

def main():
    rooms = {
        '101': {'type': 'Single', 'price': 100.0, 'booked': False},
        '102': {'type': 'Double', 'price': 150.0, 'booked': False},
        '103': {'type': 'Suite', 'price': 250.0, 'booked': False},
    }

    while True:
        print("--------Hotel Room Booking System--------")
        print("1. Display Available Rooms")
        print("2. Book Room")
        print("3. Cancel Booking")
        print("4. Show Booking Status")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_available_rooms(rooms)
        elif choice == '2':
            book_room(rooms)
        elif choice == '3':
            cancel_booking(rooms)
        elif choice == '4':
            show_booking_status(rooms)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()