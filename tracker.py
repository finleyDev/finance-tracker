
from datetime import datetime
import csv

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
        
        amount = int(input("How much did you spend"))

        date = datetime.now().strftime("%Y-%m-%d %H:%M")

        entries.append({"category" : user_kind, "amount" : amount , "date" : date})

        another = input("Add another entry? y/n")
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
            print(category)




def save_entries():
    with open("tracker.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "date"])
        writer.writeheader()
        writer.writerows(entries)
                                    

load_entries()


while True:
    print("What do you want to do?")
    print("1 for add a entrie")
    print("2 for show amount")
    print("3 for amount of a specific category")
    print("4 remove an entry")
    print("5 quit")
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
        break



save_entries()





        


    
