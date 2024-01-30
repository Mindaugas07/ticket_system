# from distances import distances
from dataclasses import dataclass
from typing import List, Dict
import os
import random

# Create a flight ticketing mini system:

# The CLI should ask you to choose departure place and destination (minimum 5 cities)
#  (Use dictionary to create a distance between the cities matrix map ).
# Then it should show options for at least 3 flight options with different aircraft
#  (Airbus A330-300, A340-300,A 340-600, A350- 100, Boeing 747-400, 747-800, 777-300).
#  Every aircraft has different seat configuration (economy, business, first with different seat amount,
#  seat pitch and average price)
# When you select the ticket (the provided option) the final cost should be calculated depending
#  on aircraft type, departure time, and fuel consumption. (We can agree that flights that departure earlier,
#  has less seats and are older, cost more). Use data classes and simple classes to achieve the result.
distances = {
    "Kaunas": {
        "Kaunas": 0.0,
        "Barcelona": 2187.0,
        "London": 1637.0,
        "Boston": 6566.0,
        "Sydney": 15364.0,
    },
    "Barcelona": {
        "Barcelona": 0.0,
        "Kaunas": 2187.0,
        "London": 1137.0,
        "Boston": 5864.0,
        "Sydney": 17180.0,
    },
    "London": {
        "London": 0.0,
        "Kaunas": 1637.0,
        "Barcelona": 1137.0,
        "Boston": 5264.0,
        "Sydney": 16994.0,
    },
    "Boston": {
        "Boston": 0.0,
        "Kaunas": 6566.0,
        "Barcelona": 5864.0,
        "London": 5264.0,
        "Sydney": 16240.51,
    },
    "Sydney": {
        "Sydney": 0.0,
        "Kaunas": 15364.0,
        "Barcelona": 17180.0,
        "London": 16994.0,
        "Boston": 16240.51,
    },
}


planes = {
    "Airbus A330-300": {
        "Seat price coef. per class": {
            "Economy": {"Early in the morning": 1.0, "Early": 1.5, "Late": 1.0},
            "Premium Economy": {"Early in the morning": 2.0, "Early": 2.5, "Late": 2.0},
            "Business class": {"Early in the morning": 5.0, "Early": 6.5, "Late": 5.0},
        },
        "Fuel consumption coef.": 9.5,
    },
    "Boeing 747-400": {
        "Seat price coef. per class": {
            "Economy": {"Early in the morning": 1.0, "Early": 1.5, "Late": 1.0},
            "Premium Economy": {"Early in the morning": 3.0, "Early": 3.6, "Late": 3.0},
            "Business class": {"Early in the morning": 6.0, "Early": 7.2, "Late": 6.0},
        },
        "Fuel consumption coef.": 10.0,
    },
}


# @dataclass
# class TicketSystem:
#     flights: List["Flight"]

#     def add_flight(self, flight: "Flight") -> None:
#         if flight not in self.flights:
#             self.flights.append(flight)

#     def remove_flight(self, flight: "Flight") -> None:
#         if flight in self.flights:
#             self.flights.remove(flight)

#     def get_flights(self) -> List["Flight"]:
#         return self.flights


@dataclass
class Flight:
    time_options = ["Early in the morning", "Early", "Late"]

    id: str
    departure_city: str
    arrival_city: str
    time_of_departure: str

    @staticmethod
    def flight_id_generator():
        return "EFL" + str(random.randint(1000, 9999))

    @classmethod
    def time_of_travel(cls):
        day_time = random.choice(Flight.time_options)
        return day_time

    def get_flight_distance(self) -> float:
        return distances[self.departure_city][self.arrival_city]

    @staticmethod
    def get_plane():
        planes_list = list(planes.keys())
        plane = random.choice(planes_list)
        return plane

    @classmethod
    def get_seat_class(cls):
        plane_name = Flight.get_plane()
        seat_classes_list = list(
            planes[plane_name]["Seat price coef. per class"].keys()
        )
        seat = random.choice(seat_classes_list)
        return seat

    def get_price(self) -> float:
        time = Flight.time_of_travel()
        plane = Flight.get_plane()
        seat = Flight.get_seat_class()
        print(plane)
        return round(
            (
                self.get_flight_distance()
                * planes[plane]["Fuel consumption coef."]
                * planes[plane]["Seat price coef. per class"][seat][time]
                * 0.01
            ),
            2,
        )

    def __str__(self) -> str:
        return f"Flight {self.flight_id_generator()}, class: {self.get_seat_class()}, departure city: {self.departure_city}, arrival city: {self.arrival_city}, leaves: {self.time_of_travel()}, price: {self.get_price()} USD."


departure = ""
destinations = list(distances.keys())


def print_destinations(*args):
    if args:
        city = args[0]
        print(f"You will travel from {city} to: ")
        destinations.remove(*args)
        for row, key in enumerate(destinations):
            print((row + 1), "--", key)
    else:
        for row, key in enumerate(destinations):
            print((row + 1), "--", key)


if __name__ == "__main__":
    os.system("cls")
    user_option = "1"
    print("Welcome to 'Earth is flat' airways, please choose your departure city:")
    print_destinations()
    while True:
        try:
            user_option = input(
                f"""
99.  'Exit'
"""
            )
        except:
            print("Wrong input. Please enter a number from the list...")
            break
        if user_option == "1":
            if departure is "":
                departure = destinations[0]
                os.system("cls")
                print_destinations(departure)
            else:
                arrival = destinations[0]

        elif user_option == "2":
            if departure is "":
                departure = destinations[1]
                os.system("cls")
                print_destinations(departure)
            else:
                arrival = destinations[1]

        elif user_option == "3":
            if departure is "":
                departure = destinations[2]
                os.system("cls")
                print_destinations(departure)
            else:
                arrival = destinations[2]

        elif user_option == "4":
            if departure is "":
                departure = destinations[3]
                os.system("cls")
                print_destinations(departure)
            else:
                arrival = destinations[3]

        elif user_option == "5" and departure is "":
            departure = destinations[4]
            os.system("cls")
            print_destinations(departure)

        elif user_option == "99":
            os.system("cls")
            print("We can offer you these flights: ")
            break

        else:
            os.system("cls")
            print("Wrong input. Please enter a number from the list...")
            print_destinations()

# print(departure, arrival)


flight_one = Flight(
    id=Flight.flight_id_generator(),
    departure_city=departure,
    arrival_city=arrival,
    time_of_departure=Flight.time_of_travel(),
    # plane="Airbus A330-300",
    # seat_class="Business class",
)
flight_two = Flight(
    id=Flight.flight_id_generator(),
    departure_city=departure,
    arrival_city=arrival,
    time_of_departure=Flight.time_of_travel(),
    # plane="Airbus A330-300",
    # seat_class="Business class",
)
flight_three = Flight(
    id=Flight.flight_id_generator(),
    departure_city=departure,
    arrival_city=arrival,
    time_of_departure=Flight.time_of_travel(),
    # plane="Airbus A330-300",
    # seat_class="Business class",
)

print(flight_one)
print(flight_two)
print(flight_three)
