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
        header = f.readline()
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, start_str, priority, estimate, completion = line.split("\t")
            projects.append(
                Project(name, parse_date(start_str), int(priority), float(estimate), int(completion))
            )
    return projects

def display_projects(projects: List[Project]) -> None:
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    incomplete.sort()  # 按 priority
    complete.sort()
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")

def filter_projects_by_date(projects: List[Project]) -> None:
    date_str = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    try:
        cutoff = parse_date(date_str)
    except ValueError:
        print("Invalid date format.")
        return
    filtered = [p for p in projects if p.starts_after(cutoff)]
    filtered.sort(key=lambda p: p.start_date)
    for p in filtered:
        print(p)

def add_new_project(projects: List[Project]) -> None:
    print("Let's add a new project")
    name = input("Name: ").strip()
    start_str = input("Start date (dd/mm/yyyy): ").strip()
    priority = int(input("Priority: ").strip())
    estimate = float(input("Cost estimate: $").strip().replace("$", ""))
    completion = int(input("Percent complete: ").strip())
    new_proj = Project(name, parse_date(start_str), priority, estimate, completion)
    projects.append(new_proj)
    print("Added:", new_proj)

def list_projects_indexed(projects: List[Project]) -> None:
    for i, p in enumerate(projects):
        print(f"{i} {p}")

def update_project(projects: List[Project]) -> None:
    list_projects_indexed(projects)
    try:
        idx = int(input("Project choice: ").strip())
        proj = projects[idx]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return
    print(proj)
    new_pct = input("New Percentage: ").strip()
    if new_pct != "":
        proj.completion = int(new_pct)
    new_pri = input("New Priority: ").strip()
    if new_pri != "":
        proj.priority = int(new_pri)
def update_project(projects: List[Project]) -> None:
    list_projects_indexed(projects)
    try:
        idx = int(input("Project choice: ").strip())
        proj = projects[idx]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return
    print(proj)
    new_pct = input("New Percentage: ").strip()
    if new_pct != "":
        proj.completion = int(new_pct)
    new_pri = input("New Priority: ").strip()
    if new_pri != "":
        proj.priority = int(new_pri)

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
        "- (S)ave projects\n"      
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"  
        "- (A)dd new project\n"    
        "- (U)pdate project\n"
        "- (Q)uit\n"
    )
    while True:
        print(MENU)
        choice = input(">>> ").strip().lower()
        if choice == "l":
            filename = input("File to load: ").strip() or DEFAULT_FILENAME
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("File to save to: ").strip() or DEFAULT_FILENAME
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            break
        else:
            print("Invalid choice")

    print("Goodbye.")


if __name__ == "__main__":
    main()
