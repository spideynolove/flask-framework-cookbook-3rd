from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/hung/sqlite3/database/test.db'

db = SQLAlchemy(app)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

with app.app_context():
    db.create_all()