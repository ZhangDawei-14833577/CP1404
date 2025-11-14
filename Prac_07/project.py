"""Project class
Estimate: 30 minutes
Actual:   0 minutes (fill when done)
"""

from dataclasses import dataclass
from datetime import date
from typing import Any


@dataclass
class Project:
    """Represent a project with basic fields."""
    name: str
    start_date: date
    priority: int
    estimate: float
    completion: int  # 0-100


    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Project):
            return NotImplemented
        return self.priority < other.priority

    def is_complete(self) -> bool:
        return self.completion >= 100

    def starts_after(self, d: date) -> bool:
        return self.start_date >= d

    def __str__(self) -> str:
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.estimate:,.2f}, "
                f"completion: {self.completion}%")


    def to_tsv_row(self) -> str:
        return "\t".join([
            self.name,
            self.start_date.strftime("%d/%m/%Y"),
            str(self.priority),
            f"{self.estimate}",
            str(self.completion),
        ])
