"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the numerator or denominator entered by the user is not a valid integer, such as the letters abc or
    the floating point number 1.1.
2. When will a ZeroDivisionError occur?
    When the denominator entered by the user is 0, a ZeroDivisionError occurs.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")