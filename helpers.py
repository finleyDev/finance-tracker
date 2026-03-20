import csv

def load_entries():
    entries = []
    try:
        with open("tracker.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                entries.append(row)

    except FileNotFoundError:
        pass
    return entries


def save_entries(entries):
    try:
        with open("tracker.csv" , "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["category", "amount", "date"])
            writer.writeheader()
            writer.writerows(entries)

    except FileNotFoundError:
        pass

