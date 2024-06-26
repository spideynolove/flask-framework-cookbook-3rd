import ccy
from flask import Flask, request
from my_app.product.views import product_blueprint
from markupsafe import Markup

app = Flask(__name__)
app.register_blueprint(product_blueprint)


@app.template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:]) or 'USD'
    return '{0} {1}'.format(currency_code, amount)


@app.template_filter('product_color')
def product_color_filter(product_name):
    product_colors = {
        'iPhone': 'orange-text',
        'Samsung': 'purple-text',
        'iPad': 'green-text',
        'Google': 'red-text',
        'Sony': 'blue-text',
        'LG': 'pink-text',
        'Nokia': 'cyan-text',
        'Xiaomi': 'yellow-text',
    }
    brand = product_name.split(' ', 1)[0]
    return product_colors.get(brand, 'black-text')


class momentjs:
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, format):
        return Markup(
            "<script>\ndocument.write(moment(\"%s\").%s);\n</script>" % (
                self.timestamp.strftime("%Y-%m-%dT%H:%M:%S"), format
            )
        )

    def format(self, fmt):
        return self.render("format(\"%s\")" % fmt)

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")


# Set jinja template global
app.jinja_env.globals['momentjs'] = momentjs
