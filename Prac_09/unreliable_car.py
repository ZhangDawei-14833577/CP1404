"""UnreliableCar class that inherits from Car."""

from random import randint
from car import Car


class UnreliableCar(Car):
    """Specialised Car that only sometimes drives, based on reliability."""

    def __init__(self, name: str, fuel: float, reliability: float):
        """Initialise an UnreliableCar with name, fuel and reliability percentage."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance: float) -> float:
        """Attempt to drive the given distance.

        Drive only if a random number (0-100) is less than reliability.
        Return the distance actually driven (0 or the normal Car.drive result).
        """
        random_number = randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        return 0.0

