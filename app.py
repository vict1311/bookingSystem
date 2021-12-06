from flask import Flask, render_template, redirect, url_for, request
from cs50 import SQL

# we use url_for to get urls for every html page we route to. this takes the name of an html file and 
# gives us a url for this

app = Flask(__name__)
db = SQL('sqlite:///database/bookings.db')

# create Booking class that we can load instances of
class Booking:
    def __init__(self, itemName, fullName, startDate, endDate, email):
        self.itemName = itemName
        self.fullName = fullName
        self.startDate = startDate
        self.endDate = endDate
        self.email = email


# hardcode bookings using our Booking class
# booking1 = db.execute('SELECT * FROM bookings WHERE id=1')
# Booking("Drill", "Victor Jensen", "2021-11-19", "2021-11-20", "villerdk@hotmail.com")
# booking2 = db.execute('SELECT * FROM bookings WHERE id=2')
# Booking("Ladder", "Trine Andersen", "2021-11-19", "2021-11-23", "tandersen@example.com")
# booking3 = db.execute('SELECT * FROM bookings WHERE id=3')
# Booking("Chairs", "Emil Bo", "2021-12-19", "2021-12-30", "e18bo@example.com")


#when a booking is created the booking is added to bookingList with .append(), so bookingList.append(NameOfBooking)
#when we append this later, we just use .append(Booking(variableFromPopup1, variableFromPopup2, etc.))

@app.route("/") 
def landing():
    return render_template("landing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")    

@app.route("/catalogue", methods=["GET", "POST"])
# we use both GET and POST methods, since POST isnt default
def catalogue():
    if request.method == "GET": 
        return render_template("catalogue.html")
        #if the user requests to GET data (get data from resource) we show them our page
    else:
        #if the user requests to POST data (send data to resource) we take info from our HTML form and save it as variables
        itemName = request.form.get("itemName")
        fullName = request.form.get("fullName")
        startDate = request.form.get("startDate")
        endDate = request.form.get("endDate")
        email = request.form.get("email")
        
        db.execute('INSERT INTO bookings (itemName, fullName, startDate, endDate, email) VALUES (:itemName, :fullName, :startDate, :endDate, :email)', itemName=itemName, fullName=fullName, startDate=startDate, endDate=endDate, email=email )

        bookingid = db.execute('SELECT id FROM bookings WHERE itemName=? AND fullName=? AND startDate=? AND endDate=? AND email=?', itemName, fullName, startDate, endDate, email)
        bookingList = db.execute('SELECT * FROM bookings')
    
        # we append our mock-up database
        # bookingList.append(Booking(itemName, fullName, startDate, endDate, email))
        return render_template("confirmation.html", bookingid = bookingid, bookingList = bookingList)  

@app.route("/bookings", methods=["GET", "POST"])
def bookings():
    bookingList = db.execute('SELECT * FROM bookings')
    if request.method == "GET": 
        return render_template("bookings.html", bookingList = bookingList)
        #if the user requests to GET data (get data from resource) we show them our page
    else:
        #if the user requests to POST data (send data to resource) we take info from our HTML form and save it as variables
        bookingid = request.form.get("bookingid")
        # we remove from our mock database by going through every entry in the bookingList
        for booking in bookingList:
            if booking["id"] == int(bookingid):
                db.execute('DELETE FROM bookings WHERE id=?', bookingid)
                return redirect("/bookings")
            
        return redirect("/failure")
        # return redirect("/failure") - we return failure here because we want it to happen if no row in booking list has the entered booking ID. 


@app.route("/failure")
def failure():
    return render_template("failure.html")
