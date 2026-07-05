'''
Movie Ticket Booking System

Features:

Display movies
Select seats
Calculate bill
Generate ticket
'''

def display_movies():
    print("\nAvailable Movies:")
    for movie_id, movie_info in movies.items():
        print(f"{movie_id} - {movie_info['type']} - {movie_info['name']} - Price: ${movie_info['price']:.2f} - Available Seats: {movie_info['available_seats']}")


def select_seats():
    global num_seats
    movie_id = input("\nSelect the movie to select seats (enter movie ID): ")
    if movie_id not in movies:
        print("Invalid movie ID.")
        return

    print(f"Seats for {movies[movie_id]['name']} are available {movies[movie_id]['available_seats']}. Please select the number of seats you want to book.")
    try:
        num_seats = int(input("Enter the number of seats: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if num_seats > movies[movie_id]['available_seats']:
        print("Not enough seats available.")
        return

    movies[movie_id]['available_seats'] -= num_seats
    movies[movie_id]['booked_seats'] += num_seats
    print(f"Seats successfully booked for '{movies[movie_id]['name']}!'")
   

def calculate_bill():
    movie_id = input("\nEnter the movie ID to calculate the bill: ")
    if movie_id not in movies:
        print("Invalid movie ID.")
        return

    #num_seats = movies[movie_id]['booked_seats']
    total_bill = num_seats * movies[movie_id]['price']
    print(f"Total bill for {num_seats} seats of {movies[movie_id]['name']} is: ${total_bill:.2f}")


def generate_ticket():
    movie_id = input("Enter the movie ID for the ticket: ")
    if movie_id not in movies:
        print("Invalid movie ID.")
        return

    #num_seats = movies[movie_id]['booked_seats']
    print("------Ticket-------")
    print(f"Movie: {movies[movie_id]['name']}")
    print(f"Seats Booked: {num_seats}")
    print(f"Total Amount: ${num_seats * movies[movie_id]['price']:.2f}")
    print("--------------------")


def main():
    global movies
    movies = {
        "1": {"name":"The Shawshank Redemption","type": "Drama", "price": 10.0, "booked_seats": 0,"available_seats": 10},
        "2": {"name":"The Godfather","type": "Crime", "price": 12.0, "booked_seats": 2,"available_seats": 8},
        "3": {"name":"The Dark Knight","type": "Action", "price": 15.0, "booked_seats": 0,"available_seats": 10},
        "4": {"name":"Pulp Fiction","type": "Crime", "price": 11.0, "booked_seats": 0,"available_seats": 10}
     }
    while True:
        print("--------Movie Ticket Booking System--------")
        print("1. Display Movies")
        print("2. Select Seats")
        print("3. Calculate Bill")
        print("4. Generate Ticket")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ")
        except:
            print("\nInput error. Please try again.")
            continue

        if choice == '1':
            display_movies()
        elif choice == '2':
            select_seats()
        elif choice == '3':
            calculate_bill()
        elif choice == '4':
            generate_ticket()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()