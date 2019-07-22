# -*- coding: utf-8 -*
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/second")
def seconde():
    return "https://www.developpez.net/forums/d584296/webmasters-developpement-web/balisage-x-html-validation-w3c/html-chemin-absolu-d-image/"


if __name__== "__main__":
    app.run()