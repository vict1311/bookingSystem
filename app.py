from flask import Flask, render_template, redirect, url_for  

# we use url_for to get urls for every html page we route to. this takes the name of an html file and 
# gives us a url for this

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")    

@app.route("/catalogue")
def catalogue():
    return render_template("catalogue.html")

@app.route("/bookings")
def bookings():
    return render_template("bookings.html")        