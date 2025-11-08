"""Project Management Program
Estimate: 120 minutes
Actual:   0 minutes (fill when done)

Loads projects from a tab-delimited file and manages them via a menu.
"""

from datetime import datetime, date
from typing import List
from project import Project

DEFAULT_FILENAME = "projects.txt"


def parse_date(d: str) -> date:
    return datetime.strptime(d, "%d/%m/%Y").date()


def load_projects(filename: str) -> List[Project]:
    projects: List[Project] = []
    with open(filename, "r", encoding="utf-8") as f:
        header = f.readline()  # 丢弃表头
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, start_str, priority, estimate, completion = line.split("\t")
            projects.append(
                Project(
                    name=name,
                    start_date=parse_date(start_str),
                    priority=int(priority),
                    estimate=float(estimate),
                    completion=int(completion),
                )
            )
    return projects


def main() -> None:
    print("Welcome to Pythonic Project Management")
    try:
        projects = load_projects(DEFAULT_FILENAME)
        print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    except FileNotFoundError:
        projects = []
        print(f"No default file {DEFAULT_FILENAME}; starting empty.")

    MENU = (
        "- (L)oad projects\n"
        "- (Q)uit\n"
    )
    while True:
        print(MENU)
        choice = input(">>> ").strip().lower()
        if choice == "l":
            filename = input("File to load: ").strip() or DEFAULT_FILENAME
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "q":
            break
        else:
            print("Invalid choice")

    print("Goodbye.")


if __name__ == "__main__":
    main()
