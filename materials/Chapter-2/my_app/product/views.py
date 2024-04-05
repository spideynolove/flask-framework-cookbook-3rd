from datetime import datetime
from werkzeug.exceptions import abort
from flask import render_template
from flask import Blueprint
from my_app.product.models import PRODUCTS

product_blueprint = Blueprint('product', __name__)


@product_blueprint.context_processor
def some_processor():
    def full_name(prod):
        return '{0} / {1}'.format(prod['category'], prod['name'])

    def nick_name(prod):
        return '{0} ({1})'.format(prod['name'], prod['nickname'])
    return {'full_name': full_name, 'nick_name': nick_name}


@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS, timestamp=datetime.now())


@product_blueprint.route('/product/<key>')
def product(key):
    prod = PRODUCTS.get(key)
    if not prod:
        abort(404)
    return render_template('product.html', product=prod)
