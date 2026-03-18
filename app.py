from flask import Flask, render_template
import csv

app = Flask("__name__")

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
def home():
    entries = load_entries()
    total = sum(int(e["amount"])for e in entries)
    return render_template("index.html", entries=entries, total=total)

if __name__ == "__main__":
    app.run(debug=True)