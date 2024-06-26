from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
@app.route('/hello/<user>')
def hello_world(user=None):
    user = user or 'Hung'   # good practice to use default value
    # python format string
    return '''
<html>
    <head>
    <title>Flask Framework Cookbook</title>
    </head>
    <body>
    <h1>Hello %s!</h1>
    <p>Welcome to the world of Flask!</p>
    </body>
</html>''' % user


if __name__ == '__main__':
    app.run()
