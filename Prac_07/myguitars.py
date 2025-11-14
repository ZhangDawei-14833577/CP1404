"""
CP1404 Practical - More Guitars
Read guitars from file, display them, allow user to add more, then save all.
"""

from guitar import Guitar


FILENAME = "guitars.csv"


def main():
    """Main program to read guitars, display, sort, add new ones, and save."""
    guitars = load_guitars(FILENAME)

    print("These are the guitars in the file:")
    display_guitars(guitars)

    # sort by year (oldest first)
    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    # let user add new guitars
    print("\nEnter your new guitars (blank name to quit):")
    add_new_guitars(guitars)

    # save updated list
    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}")


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of Guitar objects."""
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """Prompt user to enter new guitars and add them to the list."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Save guitars back into CSV (overwrite)."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()