from flask import Flask, render_template


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "TphjwvUZUwVMqmDdUwhV2B8qb2es1rP8"


@app.route("/")
def home():
    return render_template("index.html", title="Home - ")


@app.route("/about_us")
def about_us():
    return render_template("about-us.html", title="About US - ")


@app.route("/destinations")
def destinations():
    return render_template("destinations.html", title="Destinations - ")


@app.route("/destinations/usa")
def destinations_usa():
    return render_template("countries/us.html", title="United States - ")


@app.route("/destinations/uk")
def destinations_uk():
    return render_template("countries/uk.html", title="United Kingdom - ")


@app.route("/destinations/spain")
def destinations_spain():
    return render_template("countries/spain.html", title="Spain - ")


@app.route("/destinations/europe")
def destinations_europe():
    return render_template("countries/europe.html", title="Europe - ")


@app.route("/destinations/turkey")
def destinations_turkey():
    return render_template("countries/turkey.html", title="Turkey - ")


@app.route("/destinations/canada")
def destinations_canada():
    return render_template("countries/canada.html", title="Canada - ")


@app.route("/services")
def services():
    return render_template("our-services.html", title="Services - ")


@app.route("/contact")
def contact():
    return render_template("contact-us.html", title="Contact - ")


#  Destinations | Services | Contact

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=3000, debug=True)
    app.run(debug=True)
