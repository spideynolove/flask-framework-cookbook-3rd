from decimal import Decimal
from flask import request, Blueprint, jsonify
from my_app.catalog.models import Product
from my_app import db

catalog = Blueprint('catalog', __name__)


@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."


@catalog.route('/product/<key>')
def product(key):
    product = Product.query.get_or_404(key)
    return 'Product - %s, $%s' % (product.name, product.price)


@catalog.route('/products')
def products():
    products = Product.query.all()
    res = {}
    for product in products:
        res[product.key] = {
            'name': product.name,
            'price': str(product.price),
        }
    return jsonify(res)


@catalog.route('/product-create', methods=['POST',])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    # key = request.form.get('key')

    last_product = Product.query.order_by(Product.key.desc()).first()
    last_key = last_product.key if last_product else 0
    # print(last_key)

    product = Product(
        name=name,
        price=price,
        key=last_key + 1
    )

    # product.save()
    db.session.add(product)
    db.session.commit()
    return 'Product created.'