
FILENAME = "wimbledon.csv"

def load_data(filename):
    """Load CSV and return a list of lists (rows split by comma)."""
    rows = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
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

def get_champion_countries(rows):
    """Return a sorted list of distinct champion countries."""
    countries = {row[1] for row in rows}
    return sorted(countries)

def main():
    data = load_data(FILENAME)
    champions = count_champions(data)
    countries = get_champion_countries(data)

    print("Wimbledon Champions:")
    for name, titles in champions.items():
        print(f"{name} {titles}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
