# -*- coding: utf-8 -*
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/kali")
def hello():
    return render_template("hello.html")

@app.route("/")
def effets():
    return render_template("thirdPage.html")

if __name__== "__main__":
    app.run()