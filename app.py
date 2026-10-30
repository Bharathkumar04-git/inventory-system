from flask import Flask, render_template, request, redirect

app = Flask(__name__)

stock = []
# items with quantity below this number are shown as low stock
LOW_STOCK_LIMIT = 10


# find the items that are running low
def get_low_stock():
    low_items = []
    for item in stock:
        if item["quantity"] < LOW_STOCK_LIMIT:
            low_items.append(item)
    return low_items

@app.route("/")
def home():
    low_stock = get_low_stock()
    return render_template("index.html", stock=stock, low_stock=low_stock, version="v3")

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