"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):    # Revise 2(Change all code "month" to "number_of_month")
        income = float(input(f"Enter the income for month {month}:"))    # Revise 1
        incomes.append(income)

    print_income_report(incomes, number_of_months)

def print_income_report(incomes, number_of_months):     # Revise 3(Add a suitable function name)
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()