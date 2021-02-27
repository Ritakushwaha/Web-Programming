class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    #CALCULATE AVAILABLE SEATS
    def open_seats(self):
        return self.capacity - len(self.passengers)

    #ADD PASSENGERS IF SEAT AVAILABLE
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True



flight = Flight(5)

people = ["Rita", "Girwar", "Priyanshi", "Vijaya", "Pragya", "Preet"]

for person in people:
    if flight.add_passenger(person):
        print(f"Passenger {person} is added successfully.")
    else:
        print(f"No seats available for {person}.")
