from flask import Flask
from flask_mongoengine import MongoEngine
# from redis import Redis


app = Flask(__name__)

# app.config['MONGODB_SETTINGS'] = {'flask_db': 'my_catalog'}

app.config["MONGODB_SETTINGS"] = [
    {
        "db": "my_catalog",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }
]
db = MongoEngine(app)

# app.debug = True
# db.init_app(app)

# redis = Redis()

from my_app.catalog.views import catalog
app.register_blueprint(catalog)