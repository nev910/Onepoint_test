import string
import random
from colors import bcolors

global nb_availability
user_booked_seat = {}


def generate_seats_arrangement(num_passengers, code_avion):
    rows = list(range(1, num_passengers))
    seats = list(string.ascii_uppercase)[:code_avion]

    seats_arrangement = {}
    seat_count = 0

    for row in rows:
        for seat in seats:
            if seat_count < num_passengers:
                seat_number = str(row) + seat
                seats_arrangement[seat_number] = {'available': True}
                seat_count += 1
            else:
                break
        if seat_count >= num_passengers:
            break

    return seats_arrangement


def test_random_book(seats_arrangement, nb_booked):
    seat_numbers = list(seats_arrangement.keys())
    random_seat_numbers = random.sample(seat_numbers, nb_booked)
    for seat_number in random_seat_numbers:
        seats_arrangement[seat_number]['available'] = False
    return seats_arrangement


def show_plan_seat(seats_arrangement, column_range_flight):
    i = 0
    for seat in seats_arrangement:
        if i == column_range_flight:
            print()
            i = 0
        if seats_arrangement[seat]['available']:
            print(f"▢ {bcolors.OK_GREEN}{seat}{bcolors.ENDC}", end=" ")
        else:
            print(f"▢ {bcolors.KO_RED}{seat}{bcolors.ENDC}", end=" ")
        i += 1
    print()


def book_seat(seats_arrangement):
    while True:
        try:
            input_nb_book = int(input("Please enter the number of seats booking: "))
            if input_nb_book <= nb_availability:
                i = 0
                while i != input_nb_book:
                    input_seat = input("Please enter the seat number: ")
                    if input_seat in seats_arrangement:
                        if seats_arrangement[input_seat]['available']:
                            seats_arrangement[input_seat]['available'] = False
                            user_booked_seat[i] = input_seat
                            i += 1
                        else:
                            print("Seat already booked. Please enter a valid seat.")
                    else:
                        print("Invalid seat. Please enter a valid seat.")
                return seats_arrangement
        except Exception:
            print("Invalid input. Please enter a valid integer.")


def ticket_generation(type_avion):
    list_avion_details = {1: "Boeings court-courrier A220", 2: "Boeings moyen courrier Boeing A350",
                          3: "Boeings long courrier Boieng A330"}

    print("-------------Thank you for booking !----------")
    print("-------------Here is your ticket !----------")
    print("----------------------------------------------")
    print(f"-     	{list_avion_details[type_avion]}   		 -")
    print()
    for seat in user_booked_seat:
        print(f" 			Your seat is {user_booked_seat[seat]}")
    print("----------------------------------------------")


list_avion = [1, 2, 3]
list_nb_passenger = [148, 279, 224]
list_range_avion = [6, 9, 8]

while True:
    print("----------------------------------------------")
    print("-                 Bienvenue!                 -")
    print("----------------------------------------------")
    print("Veuillez choisir le type d'avion:")
    print("Boeings court-courrier A220 => Select 1")
    print("Boeings moyen courrier Boeing A350 => Select 2")
    print("Boeings long courrier Boieng A330 => Select 3")
    print()
    input_type_avion = input("Select a number: ")
    try:
        input_type_avion = int(input_type_avion)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    if input_type_avion not in list_avion:
        print("Invalid input. Please enter a valid integer.")
    else:
        print(f"Your input {input_type_avion} is valid.")
        nb_passenger = list_nb_passenger[input_type_avion - 1]
        column_range_flight = list_range_avion[input_type_avion - 1]
        plan_avion = generate_seats_arrangement(nb_passenger, column_range_flight)

        # generate a fake reservation
        random_booked = random.randrange(nb_passenger)
        test_dict = test_random_book(plan_avion, random_booked)

        nb_availability = nb_passenger - random_booked
        print(f"There is only {nb_availability} seats available !")
        show_plan_seat(test_dict, column_range_flight)

        a = book_seat(test_dict)
        show_plan_seat(a, column_range_flight)

        ticket_generation(input_type_avion)
        print()
