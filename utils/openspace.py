from .table import Seat, Table
'''I imported Seat class and Table class from the file table.py. 
Struggled a little bit here because at first I didn't put the dot before table
so python did not recognise the module and there was always an error. '''

import random
class Openspace:
    def __init__(self, number_of_tables):
        '''Here I created the attribute number_of_tables. Thanks to that I was able to create 6 tables inside the openspace. '''
        self.number_of_tables = number_of_tables
        self.tables = []
        for i in range(number_of_tables):
            new_table = Table(4)
            self.tables.append(new_table)
    def organize(self, names):
        for name in names:
            placed = False
            while not placed:
                '''The loop was created to continue until the name finds a place.'''
                table = random.choice(self.tables)
                '''Thanks to the library random that I imported the places are randomly
                  assigned and are not the same each time the code runs. '''
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