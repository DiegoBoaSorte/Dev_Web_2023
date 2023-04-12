from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def index():
      return render_template("home.html")

@app.route("/quemsomos")
def who():
    return render_template("quemsomos.html")

@app.route("/contato")
def cadastro():
    return render_template("contato.html")

