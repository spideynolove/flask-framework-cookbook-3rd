import requests

items = {
    # "iphone-12": {"name": "iPhone 12", "price": 999.0},
    
    # "ipad-pro": {"name": "iPad Pro", "price": 799.0},
    # "macbook-pro": {"name": "MacBook Pro", "price": 1499.0},
    
    # "samsumg-galaxy": {"name": "Samsung Galaxy", "price": 499.0},
    # "huawei-mate": {"name": "Huawei Mate", "price": 399.0},
    # "xiao-mi": {"name": "Xiao Mi", "price": 299.0},
    # "sony-xperia": {"name": "Sony Xperia", "price": 399.0},
    # "one-plus": {"name": "One Plus", "price": 499.0},
    # "google-pixel": {"name": "Google Pixel", "price": 399.0},
    # "lg-v60": {"name": "LG V60", "price": 299.0},
    # "nokia-lumia": {"name": "Nokia Lumia", "price": 199.0},
    # "blackberry-key": {"name": "Blackberry Key", "price": 299.0},
    # "htc-u": {"name": "HTC U", "price": 199.0},
    # "motorola-edge": {"name": "Motorola Edge", "price": 299.0},
    # "oppo-find": {"name": "Oppo Find", "price": 399.0},
    # "vivo-x": {"name": "Vivo X", "price": 299.0},
    # "realme-pro": {"name": "Realme Pro", "price": 199.0},

    # "lenovo-k": {"name": "Lenovo K", "price": 199.0},
    # "asus-rog": {"name": "Asus ROG", "price": 299.0},
    # "acer-predator": {"name": "Acer Predator", "price": 199.0},
    # "msi-gaming": {"name": "MSI Gaming", "price": 299.0},
    # "razer-blade": {"name": "Razer Blade", "price": 199.0},
    # "alienware-area": {"name": "Alienware Area", "price": 299.0},
    # "hp-omen": {"name": "HP Omen", "price": 199.0},
    # "dell-g": {"name": "Dell G", "price": 299.0},

    "iphone-12": {"name": "iPhone 12", "price": 999.0, 'category': 'smartphone'},
    "ipad-pro": {"name": "iPad Pro", "price": 799.0, 'category': 'tablet'},
    "macbook-pro": {"name": "MacBook Pro", "price": 1499.0, 'category': 'laptop'},
    "samsumg-galaxy": {"name": "Samsung Galaxy", "price": 499.0, 'category': 'smartphone'},
    "alienware-area": {"name": "Alienware Area", "price": 299.0, 'category': 'laptop'},
    "motorola-edge": {"name": "Motorola Edge", "price": 299.0, 'category': 'smartphone'},
    "asus-rog": {"name": "Asus ROG", "price": 299.0, 'category': 'laptop'},
    "realme-pro": {"name": "Realme Pro", "price": 199.0, 'category': 'smartphone'},
    "dell-g": {"name": "Dell G", "price": 299.0, 'category': 'laptop'},
    "htc-u": {"name": "HTC U", "price": 199.0, 'category': 'smartphone'},
    "hp-omen": {"name": "HP Omen", "price": 199.0, 'category': 'laptop'},
    "nokia-lumia": {"name": "Nokia Lumia", "price": 199.0, 'category': 'smartphone'},
    "acer-predator": {"name": "Acer Predator", "price": 199.0, 'category': 'laptop'},
    "blackberry-key": {"name": "Blackberry Key", "price": 299.0, 'category': 'smartphone'},
    "msi-gaming": {"name": "MSI Gaming", "price": 299.0, 'category': 'laptop'},
    "vivo-x": {"name": "Vivo X", "price": 299.0, 'category': 'smartphone'},
}

for item in items:
    res = requests.post(
        "http://127.0.0.1:5000/product-create",
        # data={"key": item, "name": items[item]["name"], "price": items[item]["price"]},
        data={"key": item, "name": items[item]["name"], "price": items[item]["price"], "category": items[item]["category"]},
    )