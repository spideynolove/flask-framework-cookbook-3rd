from flask import Blueprint
from my_app.hello.models import MESSAGES

hello = Blueprint('hello', __name__)


# @hello.route('/')
@hello.route('/hello')
def hello_world():
    return MESSAGES['default']


@hello.route('/read/hello/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key


@hello.route('/create/hello/<key>/<message>')
def create_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Created/Updated" % key


@hello.route('/delete/hello/<key>')
def delete_message(key):
    del MESSAGES[key]
    return "%s Deleted" % key
