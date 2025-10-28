"""
Guitar class
Estimate: 30 minutes
Actual:  minutes
"""

class guitar:
    """Represent a guitar object."""
    def __init__(self, name, year, cost):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost
    def get_age(self):
        """Return how old the giutar is in years."""
    def is_vintage(self):
    """Return True if the guitar is 50 or more years old."""
    def __str__(self):
        """Return nicely formatted string of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
