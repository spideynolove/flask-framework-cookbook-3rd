from flask import render_template, request, Blueprint

hello = Blueprint('hello', __name__)


@hello.route('/')
@hello.route('/hello')
def hello_world():
    user = request.args.get('user', 'Hung')
    return render_template('index.html', user=user)