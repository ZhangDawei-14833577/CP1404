"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

if __name__ == "__main__":
    main()