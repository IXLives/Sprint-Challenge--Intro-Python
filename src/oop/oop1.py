# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# Vehicle is the base class
class Vehicle():
    # Base class
    def __init__(self, name):
        self.name = name
    pass

# Flight vehicles, descended from Vehicle.


class FlightVehicle(Vehicle):
    # Base of this tree
    def __init__(self, name):
        super().__init__(name)
    pass


class Airplane(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)
    pass


class StarShip(FlightVehicle):
    def __init__(self, name):
        super().__init__(name)
    pass

# Ground Vehicles, descended from Vehicle


class GroundVehicle(Vehicle):
    # Base of this tree
    def __init__(self, name):
        super().__init__(name)
    pass


class Car(GroundVehicle):
    def __init__(self, name):
        super().__init__(name)
    pass


class Motorcycle(GroundVehicle):
    def __init__(self, name):
        super().__init__(name)
    pass
