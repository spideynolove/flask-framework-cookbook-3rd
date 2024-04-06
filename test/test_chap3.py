from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/hung/sqlite3/database/app.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


with app.app_context():
    db.create_all()


# @app.route('/')
# def index():
#     new_user = User(username='john_doe', email='john@example.com')
#     db.session.add(new_user)
#     db.session.commit()

#     users = User.query.all()
#     for user in users:
#         print(user.username)

#     return 'Data Modeling Example'

@app.route('/')
def index():
    existing_user = User.query.filter_by(username='john_doe').first()
    if not existing_user:
        new_user = User(username='john_doe', email='john@example.com')
        db.session.add(new_user)
        db.session.commit()
        return 'New user added: john_doe'
    else:
        users = User.query.all()
        for user in users:
            print(user.username)
        return 'User john_doe already exists'


@app.route('/add/<username>/<email>')
def add_user(username, email):
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return f'User {username} added with email {email}'
    else:
        users = User.query.all()
        for user in users:
            print(user.username)
        return f'User {username} already exists'


if __name__ == '__main__':
    app.run()
