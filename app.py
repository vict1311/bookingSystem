from flask import Flask, render_template, redirect, url_for, request


# we use url_for to get urls for every html page we route to. this takes the name of an html file and 
# gives us a url for this

app = Flask(__name__)

# create Booking class that we can load instances of
class Booking:
    def __init__(self, itemName, fullName, startDate, endDate, email):
        self.itemName = itemName
        self.fullName = fullName
        self.startDate = startDate
        self.endDate = endDate
        self.email = email


# hardcode bookings using our Booking class
booking1 = Booking("Drill", "Victor Jensen", "2021-11-19", "2021-11-20", "villerdk@hotmail.com")
booking2 = Booking("Ladder", "Trine Andersen", "2021-11-19", "2021-11-23", "tandersen@example.com")
booking3 = Booking("Chairs", "Emil Bo", "2021-12-19", "2021-12-30", "e18bo@example.com")

bookingList = [booking1, booking2, booking3]
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
        
        # we append our mock-up database
        bookingList.append(Booking(itemName, fullName, startDate, endDate, email))
        return redirect("/catalogue")

@app.route("/bookings", methods=["GET", "POST"])
def bookings():
    if request.method == "GET": 
        return render_template("bookings.html", bookingList = bookingList)
        #if the user requests to GET data (get data from resource) we show them our page
    else:
        #if the user requests to POST data (send data to resource) we take info from our HTML form and save it as variables
        itemName = request.form.get("itemName")
        fullName = request.form.get("fullName")
        startDate = request.form.get("startDate")
        endDate = request.form.get("endDate")
        email = request.form.get("email")
        
        # we remove from our mock database by going through every entry in the bookingList
        for i in bookingList:
            # we compare every attribute of the i'th object with the value in the submitted form
            if i.itemName == itemName and i.fullName == fullName and i.startDate == startDate and i.endDate == endDate and i.email == email:
                # if the above are true, we remove() the entry from the list
                bookingList.remove(i)
            #else:
                # if the entry does not work we show
             #   return redirect("/contact")

        return redirect("/bookings")