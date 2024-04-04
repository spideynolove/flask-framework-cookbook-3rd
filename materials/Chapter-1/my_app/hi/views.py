from flask import Blueprint
from my_app.hi.models import MESSAGES

hi = Blueprint('hi', __name__)


# @hi.route('/')
@hi.route('/hi')
def hi_world():
    return MESSAGES['default']


@hi.route('/read/hi/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key


@hi.route('/create/hi/<key>/<message>')
def create_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Created/Updated" % key


@hi.route('/delete/hi/<key>')
def delete_message(key):
    del MESSAGES[key]
    return "%s Deleted" % key
