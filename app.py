from flask import Flask, render_template, redirect 

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("landing.html")
