from flask import Flask, render_template, request, redirect
from helpers import load_entries, save_entries
from datetime import datetime
import csv

app = Flask(__name__)

load_entries()


@app.route("/")
@app.route("/home")
def home():
    entries = load_entries()
    total = sum(int(e["amount"])for e in entries)
    return render_template("index.html", entries=entries, total=total)

@app.route("/add", methods=["POST"])
def add():
    category = request.form["category"]
    amount = request.form["amount"]
    if not amount:
        return redirect("/home")
    
    try:
        amount = int(amount)
    except ValueError:
        return redirect("/home")
    
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    

    with open("tracker.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "date"])
        writer.writerow({"category": category, "amount": amount, "date": date})

    return redirect("/home")

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    entries = load_entries()
    entries.pop(index)
    save_entries(entries)
    return redirect("/home")




if __name__ == "__main__":
    app.run(debug=True)