from flask import Flask, render_template, request, redirect
from datetime import datetime
import csv

app = Flask(__name__)

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
    date = datetime.now().strftime("%Y-%m%d %H:%M")

    with open("tracker.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "date"])
        writer.writerow({"category": category, "amount": amount, "date": date})

    return redirect("/home")



if __name__ == "__main__":
    app.run(debug=True)