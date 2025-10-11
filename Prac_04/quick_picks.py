

import random

numbers_per_Line = 6
min_number = 1
max_number = 45

def main():
    number_of_picks = int(input("How many quick picks?"))

    for i in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))

def generate_quick_pick():
    numbers = []
    while len(numbers) < numbers_per_Line:
        number = random.randint(min_number, max_number)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

main()