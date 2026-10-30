from app import app, stock, get_low_stock

def setup_function():
    stock.clear()

def test_home_page_opens():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_add_stock():
    client = app.test_client()
    client.post("/add", data={"name": "Pen", "quantity": "50", "price": "10"})
    assert len(stock) == 1
    assert stock[0]["name"] == "Pen"
    assert stock[0]["quantity"] == 50

def test_empty_name_not_added():
    client = app.test_client()
    client.post("/add", data={"name": "", "quantity": "5", "price": "10"})
    assert len(stock) == 0

def test_negative_quantity_not_added():
    client = app.test_client()
    client.post("/add", data={"name": "Pen", "quantity": "-5", "price": "10"})
    assert len(stock) == 0

# test 5: updating quantity should work
def test_update_stock():
    client = app.test_client()
    client.post("/add", data={"name": "Pen", "quantity": "50", "price": "10"})
    client.post("/update", data={"index": "0", "quantity": "30"})
    assert stock[0]["quantity"] == 30


# test 6: negative quantity should not update
def test_update_negative_quantity():
    client = app.test_client()
    client.post("/add", data={"name": "Pen", "quantity": "50", "price": "10"})
    client.post("/update", data={"index": "0", "quantity": "-5"})
    assert stock[0]["quantity"] == 50


# test 7: updating an item that does not exist should not crash
def test_update_invalid_item():
    client = app.test_client()
    response = client.post("/update", data={"index": "5", "quantity": "10"})
    assert response.status_code == 302
# test 8: item below 10 should be in the low stock list
def test_low_stock_item_found():
    client = app.test_client()
    client.post("/add", data={"name": "Pen", "quantity": "5", "price": "10"})
    low_items = get_low_stock()
    assert len(low_items) == 1
    assert low_items[0]["name"] == "Pen"


# test 9: item with enough stock should not be in the list
def test_enough_stock_not_in_alert():
    client = app.test_client()
    client.post("/add", data={"name": "Book", "quantity": "10", "price": "50"})
    low_items = get_low_stock()
    assert len(low_items) == 0


# test 10: alert should show on the home page
def test_alert_shown_on_page():
    client = app.test_client()
    client.post("/add", data={"name": "Pen", "quantity": "2", "price": "10"})
    response = client.get("/")
    assert b"these items are low on stock" in response.data