from distances import distances
from dataclasses import dataclass
from typing import List, Dict
import os

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


planes = {
    "Airbus A330-300": {
        "Seat price coef. per class": {
            "Economy": 1.0,
            "Business": 1.5,
            "First class": 3.5,
        },
        "Fuel consumption coef.": 5.7,
    },
    "Boeing 747-400": {
        "Seat price coef. per class": {
            "Economy": 1.0,
            "Premium Economy": 1.6,
            "Business class": 3.2,
        },
        "Fuel consumption coef.": 10.0,
    },
}


@dataclass
class TicketSystem:
    flights: List["Flight"]

    def add_flight(self, flight: "Flight") -> None:
        if flight not in self.flights:
            self.flights.append(flight)

    def remove_flight(self, flight: "Flight") -> None:
        if flight in self.flights:
            self.flights.remove(flight)

    def get_flights(self) -> List["Flight"]:
        return self.flights


@dataclass
class Flight:
    id: str
    departure_city: str
    arrival_city: str
    time_of_departure: str

    def get_flight_distance(self) -> float:
        return distances[self.departure_city][self.arrival_city]

    def get_base_price(self) -> float:
        pass


# @dataclass
# class Plane:
#     id: str
#     name: str
#     seat_class: str
#     fuel_consumtion: float
# departure = ""
destinations = list(distances.keys())

if __name__ == "__main__":
    user_option = "1"
    while int(user_option) < len(destinations):
        try:
            user_option = input(
                f"""
"Welcome to 'Earth is flat' airways, please choose your departure city: ":

1.  {destinations[0]}
2.  {destinations[1]}
3.  {destinations[2]}
4.  {destinations[3]}
5.  {destinations[4]}

"""
            )
        except:
            print("Wrong input. Please enter a number ...")
        if user_option == "1":
            departure = destinations[0]
            break


print(departure)
# kun_bos = Flight(
#     id="ERT456",
#     departure_city="Kaunas",
#     arrival_city="Boston",
#     time_of_departure="Early",
#     plane="Airbus A330-300",
#     seat_class="Business class"

# )


# while True:
#     os.system("cls")
#     user_input = input(
#         "Welcome to 'Earth is flat' airways, please choose your departure city: "
#     )
