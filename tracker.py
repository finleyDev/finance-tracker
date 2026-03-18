
from datetime import datetime
import csv
from matplotlib import pyplot as plt


entries = []
kinds = ["Food",
        "Clothes",
        "Girlfriend",
        "Learn"]

def load_entries():
    try:
        with open("tracker.csv" , "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                entries.append(row)
    except FileNotFoundError:
        pass

def add_entry():
    while True:
        for i, kind in enumerate(kinds, start=1):
            print(f"{i} {kind}")
        user_kind = int(input("Where did you spend your money? type the number in"))
        
        if user_kind < 1 or user_kind > len(kinds)+ 1:
            print("Invalid input")
            continue
        if user_kind == len(kinds) + 1:
            break


        user_kind = kinds[user_kind - 1]
        
        print("How much did you spend")
        amount = int(input(">"))
        print("1 for specific date")
        print("2 for current date")
        date = input(">")
        if date == "1":
            try:
                print("What month")
                month = int(input(">"))
                print("What day?")
                day = int(input(">"))
                date = datetime(2026, month, day, 0 , 0).strftime("%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid Input")
                continue
        if date == "2":
            date = datetime.now().strftime("%Y-%m-%d %H:%M")

        entries.append({"category" : user_kind, "amount" : amount , "date" : date})

        print("Add another entry? y/n")
        another = input(">")
        if another == "n":
            break

def remove_entry():
    if not entries:
            print("Nothing to remove")
            return
    else:

        for i, entrie in enumerate(entries, start=1):
            print(f"{i} {entrie}")
        print("What entry do you want to remove")
        user_input = int(input(">"))
        if user_input < 1 or user_input > len(entries):
            print("Invalid Input")
        else:
            entries.pop(user_input-1)


def show_amount():
    total = 0
    for entry in entries:
        total = total + int(entry["amount"])
    print(f"Total spent:{total}" + " " + "€")



def show_category():
    for i, kind in enumerate(kinds, start=1):
        print(f"{i} {kind}")
    print("What amount of what category do you want to see?")
    user_input = int(input(">"))
    user_input = kinds[user_input-1]
    category = 0
    for entry in entries:
        if entry["category"] == user_input:
            category = category + int(entry["amount"])
    if category == 0:
        print(f"No entries found for {user_input}")
    else:
        print(category)




def save_entries():
    with open("tracker.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "date"])
        writer.writeheader()
        writer.writerows(entries)



def show_coordinate():
    if not entries:
        print("No entries")
        return
    for i, kind in enumerate(kinds, start=1):
        print(f"{i} {kind}")
    print(f"{len(kinds) +1 } all")
    print("What category do you want to see?")
    user_input = int(input(">"))
    if user_input > len(kinds)+1 or user_input < 1:
        return
    if user_input == len(kinds)+1:
        categories = []
        amounts = []

        for kind in kinds:
            total = sum(int(e["amount"]) for e in entries if e["category"] == kind)
            categories.append(kind)
            amounts.append(total)
        plt.bar(categories, amounts)
        plt.title("Chart")
        plt.xlabel("Category")
        plt.ylabel("€")
        plt.tight_layout()
        plt.show()
    
    else:
        kind = kinds[user_input-1]
        monthly = {}
        for e in entries:
            if e["category"] == kind:
                month = e["date"][5:7]
                if month not in monthly:
                    monthly[month] = 0
                monthly[month] += int(e["amount"])
     
        plt.plot(list(monthly.keys()), list(monthly.values()), color= "red", marker = "o")
        plt.title(f"Spending {kind}")
        plt.xlabel("Month")
        plt.ylabel("€")
        plt.tight_layout()
        plt.show()


                                   
load_entries()

while True:
    print("What do you want to do?")
    print("1 for add a entrie")
    print("2 for show amount")
    print("3 for amount of a specific category")
    print("4 remove an entry")
    print("5 for show coordinate")
    print("6 quit")
    desicion = input(">")

    if desicion == "1":
        add_entry()
    if desicion == "2":
        show_amount()
    if desicion == "3":
        show_category()
    if desicion == "4":
        remove_entry()
    if desicion == "5":
        show_coordinate()
    if desicion == "6":
        break



save_entries()





        


    
