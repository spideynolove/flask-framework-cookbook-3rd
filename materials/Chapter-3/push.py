import requests

items = {
    "iphone-12": {"name": "iPhone 12", "price": 999.0},
    "ipad-pro": {"name": "iPad Pro", "price": 799.0},
    "macbook-pro": {"name": "MacBook Pro", "price": 1499.0},
    "samsumg-galaxy": {"name": "Samsung Galaxy", "price": 499.0},
    "huawei-mate": {"name": "Huawei Mate", "price": 399.0},
    "xiao-mi": {"name": "Xiao Mi", "price": 299.0},
    "sony-xperia": {"name": "Sony Xperia", "price": 399.0},
}

for item in items:
    res = requests.post(
        "http://127.0.0.1:5000/product-create",
        data={"key": item, "name": items[item]["name"], "price": items[item]["price"]},
    )