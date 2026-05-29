from .table import Seat, Table

import random
class Openspace:
    def __init__(self, number_of_tables):
        self.number_of_tables = number_of_tables
        self.tables = []
        for i in range(number_of_tables):
            new_table = Table(4)
            self.tables.append(new_table)
    def organize(self, names):
        for name in names:
            placed = False
            while not placed:
                table = random.choice(self.tables)
                if table.left_capacity() > 0:
                    table.assign_seat(name)
                    placed = True
    def display(self):
        for i, table in enumerate(self.tables):
            occupants = []
            for seat in table.seats:
                if seat.free:
                    occupants.append("Empty")
                else:
                    occupants.append(seat.occupant)
            print(f"Table {i+1}: {occupants}")
    def store(self, filename):
        with open(filename, "w") as file:
            for i, table in enumerate(self.tables):
                file.write(f"table {i+1}: {table.seats}\n")
    def __str__(self):
        return "C'est un openspace avec 6 tables qui contiennent 4 chaises chacune"    