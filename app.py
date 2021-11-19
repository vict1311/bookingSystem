from flask import Flask, render_template, redirect, url_for  

# we use url_for to get urls for every html page we route to. this takes the name of an html file and 
# gives us a url for this

app = Flask(__name__)

# create Booking class that we can load instances of
class Booking:
    def __init__(self, itemName, personName, startDate, endDate, ID):
        self.itemName = itemName
        self.personName = personName
        self.startDate = startDate
        self.endDate = endDate
        self.ID = ID


# hardcode bookings using our Booking class
booking1 = Booking("Drill", "Victor Jensen", "19-11-2021", "20-11-2021", "villerdk@hotmail.com")
booking2 = Booking("Ladder", "Trine Andersen", "19-11-2021", "23-11-2021", "tandersen@example.com")
booking3 = Booking("Extra chair", "Emil Bo", "19-12-2021", "30-12-2021", "e18bo@example.com")

bookingList = [booking1, booking2, booking3]
#when a booking is created the booking is added to bookingList with .append(), so bookingList.append(NameOfBooking)
#when we append this later, we just use .append(Booking(variableFromPopup1, variableFromPopup2, etc.))


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
    return render_template("bookings.html", bookingList = bookingList)