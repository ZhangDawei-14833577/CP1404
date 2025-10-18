
FILENAME = "wimbledon.csv"

def load_data(filename):
    """Load CSV and return a list of lists (rows split by comma)."""
    row = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in_file:
            parts = line.strip().split(",")
            rows.append(parts)
    return rows

def count_champions(rows):
    """Return dict {champion_name: number_of_titles}."""
    champion_counts = {}
    for row in rows:
        champion = row[2]
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
    return champion_counts