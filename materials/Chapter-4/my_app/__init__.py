from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test_2.db'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/hung/Dockers/sqlite3/database/test_2.db"
db = SQLAlchemy(app)

app.secret_key = 'ABC123'

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

with app.app_context():
    db.create_all()
