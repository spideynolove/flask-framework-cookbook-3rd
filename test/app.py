from flask import Flask
from config import DevelopmentConfig


app = Flask(__name__)

# basic configuration
"""
export FLASK_APP=app.py
export FLASK_DEBUG=1
unset FLASK_APP
"""

# app.config['DEBUG'] = True
# flask run --debug # instead of export FLASK_DEBUG=1 and above line

DEBUG = True
TESTING = True

# app.config.from_object(__name__)
# app.config.from_pyfile('/path/to/config/file')

app.config.from_object(DevelopmentConfig)


@app.route('/')
def hello_world():
    return 'Hello to the World of Flask!'


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
