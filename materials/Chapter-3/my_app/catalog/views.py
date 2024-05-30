from decimal import Decimal
from flask import request, Blueprint, jsonify
from my_app.catalog.models import Product
from my_app import db   # for sqlite


catalog = Blueprint('catalog', __name__)


@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."


@catalog.route('/product/<key>')
def product(key):
    # product = Product.objects.get_or_404(key=key) # for mongoengine
    product = Product.query.get_or_404(key)
    return 'Product - %s, $%s' % (product.name, product.price)


@catalog.route('/products')
def products():
    # products = Product.objects.all()  # for mongoengine
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
    key = request.form.get('key')
    name = request.form.get('name')
    price = request.form.get('price')
    product = Product(
        key=key,
        name=name,
        price=Decimal(price)
    )

    # product.save()  # for mongoengine
    
    db.session.add(product)
    db.session.commit()
    
    return 'Product created.'
