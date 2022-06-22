from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Unilab!!'

@app.route('/new-route')
def new_route():
    return 'New route'

@app.route('/login')
def login():
    return 'Login'

if __name__ == '__main__':
    app.run(debug=True)

