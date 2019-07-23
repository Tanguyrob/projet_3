# -*- coding: utf-8 -*
from flask import Flask, render_template, request, url_for ,redirect

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        user_name = request.form['name']
        return render_template("coucou.html", name =user_name)
    else:
        user_name= request.form.get('name')
        return render_template("coucou.html", name = user_name)



@app.route("/sec")
def effets():
    return render_template("thirdPage.html")

@app.route("/kali")
def hello():
    return render_template("hello.html")

@app.route("/fct1")
def fct1(name):
    return render_template("fonction1.html", msg =name)


if __name__== "__main__":
    app.run(port=8000)