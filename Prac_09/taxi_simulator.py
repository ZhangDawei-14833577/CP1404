# taxi_simulator.py

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"

def display_taxis(taxis):
    """Display all taxis with index."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Prompt user to choose a taxi by index, return selected taxi or None if invalid."""
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        chosen_taxi = taxis[taxi_choice]
        return chosen_taxi
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


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
        if choice == "c":
            chosen_taxi = choose_taxi(taxis)
            if chosen_taxi is not None:
                current_taxi = chosen_taxi
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print("Total trip cost: $0.00")
    print("Taxis are now:")
    display_taxis(taxis)


if __name__ == "__main__":
    main()
