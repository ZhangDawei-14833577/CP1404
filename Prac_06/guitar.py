"""
Guitar class
Estimate: 30 minutes
Actual:  minutes
"""

class Guitar:
    """Represent a guitar object."""
    def __init__(self, name, year, cost):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost
    def get_age(self):
        """Return how old the giutar is in years."""
        from datetime import date
        return date.today().year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50

    def __str__(self):
        """Return nicely formatted string of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

