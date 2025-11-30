"""Test the UnreliableCar class."""

from unreliable_car import UnreliableCar


def main():
    """Test driving UnreliableCars with different reliability values."""
    # Create two vehicles: one 90% reliable and one 30% reliable.
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)
    unreliable_car = UnreliableCar("Dodgy", 100, 30)

    print("Testing reliable car:")
    for i in range(10):
        distance = reliable_car.drive(10)
        print(f"Attempt {i + 1}: drove {distance} km, fuel now {reliable_car.fuel}")

    print("\nTesting unreliable car:")
    for i in range(10):
        distance = unreliable_car.drive(10)
        print(f"Attempt {i + 1}: drove {distance} km, fuel now {unreliable_car.fuel}")


if __name__ == "__main__":
    main()
