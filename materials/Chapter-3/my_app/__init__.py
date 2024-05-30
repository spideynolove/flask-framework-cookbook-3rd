from flask import Flask
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""
app.config["MONGODB_SETTINGS"] = [
    {
        "db": "my_catalog",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }
]
db = MongoEngine(app)
"""

# from redis import Redis
# redis = Redis()

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/hung/Dockers/sqlite3/database/test.db"
db = SQLAlchemy(app)

from my_app.catalog.views import catalog

app.register_blueprint(catalog)


with app.app_context():
    db.create_all()