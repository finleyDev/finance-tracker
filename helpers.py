import csv
from matplotlib import pyplot as plt

kinds = ["Food",
        "Clothes",
        "Girlfriend",
        "Learn"]

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


def show_chart(entries):
    categories = []
    amount = []
    for kind in kinds:
        total = sum(int(e["amount"])for e in entries if e["category"]== kind)
        categories.append(kind)
        amount.append(total)
    plt.bar(categories, amount)
    plt.title("Bar")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig("static/bar.png")
    plt.close()

  

    


