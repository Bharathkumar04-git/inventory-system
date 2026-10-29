from flask import Flask, render_template, request, redirect

app = Flask(__name__)

stock = []

@app.route("/")
def home():
    return render_template("index.html", stock=stock, version="v1")


@app.route("/add", methods=["POST"])
def add_stock():
    name = request.form["name"].strip()
    quantity = int(request.form["quantity"])
    price = float(request.form["price"])

    if name != "" and quantity >= 0 and price >= 0:
        stock.append({"name": name, "quantity": quantity, "price": price})

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)