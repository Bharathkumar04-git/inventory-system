from app import app, stock

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