from my_app import db
from sqlalchemy import Sequence


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    # key = db.Column(db.String(255), nullable=False)
    key = db.Column(db.Integer, Sequence('product_key_seq'), nullable=False, unique=True)
    price = db.Column(db.Float)

    def __init__(self, key, name, price):
        self.key = key
        self.name = name
        self.price = price

    def __repr__(self):
        return '<Product %r>' % self.id