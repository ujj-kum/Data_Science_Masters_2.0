# This lab behaves as a server system
# Open https://red-fireman-ltprd.pwskills.app:5000/ in browser to access the result from client side
 
from flask import Flask
# request something from the url itself
from flask import request

app = Flask(__name__)

# Creates an url for the function
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# Creates an custom url for the function
# This URL is the API
# https://red-fireman-ltprd.pwskills.app:5000/hello1
@app.route("/hello1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"

# Creates an custom url for the function
# https://red-fireman-ltprd.pwskills.app:5000/hello2
@app.route("/hello2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"

@app.route("/test_fun")
def test():
    a = 5+6
    return "This is my first run in flask {}".format(a)

# https://red-fireman-ltprd.pwskills.app:5000/input_url?x=Ujjwal
# Below function allow to pass custom data through url to the function
@app.route("/input_url")
def request_input():
    # Request an argument and get it from URL
    # x is key, value passed during runtime
    data = request.args.get('x')
    return "This is my input from url = {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
