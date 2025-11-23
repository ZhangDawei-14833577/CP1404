# taxi_simulator.py

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    bill_to_date = 0.0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    # main loop
    while choice != "q":

        print("Invalid option")

        print(f"Bill to date: $0.00")
        print(MENU)
        choice = input(">>> ").lower()

    print("Total trip cost: $0.00")
    print("Taxis are now:")


if __name__ == "__main__":
    main()
