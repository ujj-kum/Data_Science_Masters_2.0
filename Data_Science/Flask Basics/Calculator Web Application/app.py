from flask import Flask, request, render_template
from flask import jsonify # Return result as json
import math


app = Flask(__name__)

# Renders the homepage on home location
@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/math", methods=["POST"])
def math_ops():
    if request.method=="POST":
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if ops=='add':
            res = "Sum of {} and {} is = {}".format(num1, num2, num1+num2)
        elif ops=='subtract':
            res = "Difference of {} and {} is = {}".format(num1, num2, num1-num2)
        elif ops=='multiply':
            res = "Product of {} and {} is = {}".format(num1, num2, num1*num2)
        elif ops=='divide':
            res = "Divisor of {} and {} is = {}".format(num1, num2, num1/num2)
        elif ops=='log':
            res = "Log of {} is = {}".format(num1, math.log10(num1))
        return render_template('results.html', result=res)


# Below testing of API is performed through POSTMAN App
@app.route("/postman_action", methods=["POST"])
def math_ops1():
    if request.method=="POST":
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if ops=='add':
            res = "Sum of {} and {} is = {}".format(num1, num2, num1+num2)
        elif ops=='subtract':
            res = "Difference of {} and {} is = {}".format(num1, num2, num1-num2)
        elif ops=='multiply':
            res = "Product of {} and {} is = {}".format(num1, num2, num1*num2)
        elif ops=='divide':
            res = "Divisor of {} and {} is = {}".format(num1, num2, num1/num2)
        elif ops=='log':
            res = "Log of {} is = {}".format(num1, math.log10(num1))
        
        return jsonify(res)


if __name__=="__main__":
    app.run(host="0.0.0.0")