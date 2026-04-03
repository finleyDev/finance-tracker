from flask import Flask, render_template, request, redirect, url_for
from helpers import load_entries, save_entries, show_chart
from datetime import datetime
import csv
import time

app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    entries = load_entries()
    total = sum(int(e["amount"])for e in entries)
    return render_template("index.html", entries=entries, total=total, timestamp=time.time())

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
    entries = load_entries()
    show_chart(entries)
    return redirect("/home")

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    entries = load_entries()
    entries.pop(index)
    save_entries(entries)
    show_chart(entries)
    return redirect("/home")

@app.route("/login")
def login():
    return render_template("login.html")
  




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)