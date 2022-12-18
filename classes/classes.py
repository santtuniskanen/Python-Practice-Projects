""" Write a Python program to create 
a Vehicle class with max_speed 
and mileage instance attributes.
"""

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a \
            {self.name} is {capacity} passengers"

""" Create a child class Bus that will
inherit all of the variables and methods
of the Vehicle class
"""

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
#print("Vehicle name: ", School_bus.name)