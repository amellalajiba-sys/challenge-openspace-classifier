class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None
    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False
            return f"{self.occupant} is now here"
        else:
            return "The seat is taken"
    def remove_occupant(self):
        self.occupant = None
        self.free = True

class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = []
        for i in range(capacity):
            seat_nvx = Seat() 
            self.seats.append(seat_nvx)
    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
            else:
                return False
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                seat.free = False
                return f"{name} has taken the seat"  
    def left_capacity(self):
        place_libre = 0
        for seat in self.seats:
            if seat.free:
                place_libre += 1    
        return place_libre