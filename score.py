"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    result = get_score_status(score)
    return(result)

    random_score = random.uniform(0, 100)
    return("Random score:", random_score, "Result:", get_score_status(random_score))

def get_score_status(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

main()
