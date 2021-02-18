# Make sure to not call your application flask.py because this would conflict with Flask itself.
from flask import Flask, render_template
import requests
app = Flask(__name__)

posts = requests.get("https://reqres.in/api/users?page=2").json()

print(posts)


@app.route('/')  # a router decorater
def hello_world():
    return 'Hello, World!'


@app.route('/users')
def users():
    posts['title'] = "USERS"
    # print(posts)
    return render_template('users.html', posts=posts)

# @app.route('/users')
# def users():
#     posts['title'] = "USERS"
#     print(posts)
#     return render_template('users.html', posts=posts)


if __name__ == '__main__':  # this means that if this file is run with python directly the file name is __main__
    app.run(debug=True)
