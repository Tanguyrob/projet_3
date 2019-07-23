# -*- coding: utf-8 -*
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/sec")
def effets():
    return render_template("thirdPage.html")

@app.route("/kali")
def hello():
    return render_template("hello.html")

@app.route("/fct1/<name>")
def fonction1(name):
    return "hello "+name

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        user_name = request.form['name']
        return redirect(url_for('fct1', name = user_name))
    else:
        user_name= request.form.get('name')
        return redirect(url_for('fct1', name = user_name))



if __name__== "__main__":
    app.run(port=8000)