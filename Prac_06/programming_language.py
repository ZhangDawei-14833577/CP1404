"""
Programming Language class

Estimate: 20 minutes
Actual: 30 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language."""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Refletion={self.reflection}, First appeared in {self.year}"
