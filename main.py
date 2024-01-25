# Create a flight ticketing mini system:

# The CLI should ask you to choose departure place and destination (minimum 5 cities)
#  (Use dictionary to create a distance between the cities matrix map ).
# Then it should show options for at least 3 flight options with different different aircraft
#  (Airbus A330-300, A340-300,A 340-600, A350- 100, Boeing 747-400, 747-800, 777-300).
#  Every aircraft has different seat configuration (economy, business, first with different seat amount,
#  seat pitch and average price)
# When you select the ticket (the provided option) the final cost should be calculated depending
#  on aircraft type, departure time, and fuel consumption. (We can agree that flights that are departure earlier,
#  has less seats and older, cost more). Use data classes and simple classes to achieve the result.


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
