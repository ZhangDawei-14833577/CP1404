"""
CP1404/CP5632 - Practical
Menu-driven program
"""

def main():
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == "G":
                    score = get_valid_score()
        elif choice == "P":
            print(get_score_result(score))
        elif choice == "S":
            print("*" * score)
        elif choice == "Q":
            print("Thank you!")
        else:
            print("Invalid choice")
def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = int(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score (0-100): "))
    return score
def get_score_result(score):
    """Return result string based on score value."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()
