from flask import Flask, render_template, request, redirect

app = Flask(__name__)

stock = []

@app.route("/")
def home():
    return render_template("index.html", stock=stock, version="v2")


@app.route("/add", methods=["POST"])
def add_stock():
    name = request.form["name"].strip()
    quantity = int(request.form["quantity"])
    price = float(request.form["price"])

    if name != "" and quantity >= 0 and price >= 0:
        stock.append({"name": name, "quantity": quantity, "price": price})

    return redirect("/")

# update the quantity of an existing item
@app.route("/update", methods=["POST"])
def update_stock():
    index = int(request.form["index"])
    quantity = int(request.form["quantity"])

    # only update if the item exists and quantity is not negative
    if index >= 0 and index < len(stock) and quantity >= 0:
        stock[index]["quantity"] = quantity

    return redirect("/")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)