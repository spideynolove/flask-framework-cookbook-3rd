import os
from datetime import datetime, timezone
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashlib import md5


def generate_secret_key(url, secret_key_type):
    if secret_key_type not in ["WTF_CSRF_SECRET_KEY", "APP_SECRET_KEY"]:
        raise ValueError(
            "Invalid secret_key_type. Must be 'WTF_CSRF_SECRET_KEY' or 'APP_SECRET_KEY'."
        )
    salt = "a9FsJH8DqWbXc4LzY7PvK2MnR6GtOpQiV1UvNr"
    current_time = datetime.now(tz=timezone.utc)
    formatted_time = current_time.strftime("%Y%m%d%H%M")
    base_string = f"{url}{formatted_time}{salt}{secret_key_type}"
    secret_key = md5(base_string.encode("utf-8")).hexdigest()
    return secret_key


ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/my_app_test/static/uploads'
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:////home/hung/Dockers/sqlite3/database/test_3.db"
)

url = "http://127.0.0.1:5000/"
app.config["WTF_CSRF_SECRET_KEY"] = generate_secret_key(url, "WTF_CSRF_SECRET_KEY")
app.secret_key = generate_secret_key(url, "APP_SECRET_KEY")

db = SQLAlchemy(app)
from my_app_test.catalog.views import catalog

app.register_blueprint(catalog)

with app.app_context():
    db.create_all()
