from flask import Flask, render_template


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "TphjwvUZUwVMqmDdUwhV2B8qb2es1rP8"


@app.route("/")
def home():
    return render_template("index.html", title="Home - ")


@app.route("/index")
def index():
    return render_template("new-temp/templates/index.html")


@app.route("/about")
def about_us():
    return render_template("about.html", title="About US - ")


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


@app.route("/service")
def services():
    return render_template("service.html", title="Services - ")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact - ")


@app.route("/faq")
def faq():
    return render_template("faq.html", title="FAQs - ")


@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html", title="Testimonial - ")


@app.route("/training")
def training():
    return render_template("training.html", title="Training - ")


@app.route("/us")
def us():
    return render_template("sub/us.html", title="United States - ")


@app.route("/canada")
def canada():
    return render_template("sub/canada.html", title="Canada - ")


@app.route("/uk")
def uk():
    return render_template("sub/uk.html", title="United Kingdom - ")


@app.route("/spain")
def spain():
    return render_template("sub/spain.html", title="Spain - ")


@app.route("/turkey")
def turkey():
    return render_template("sub/turkey.html", title="Turkey - ")


@app.route("/europe")
def europe():
    return render_template("sub/europe.html", title="Europe - ")


@app.route("/france")
def france():
    return render_template("sub/france.html", title="France - ")


@app.route("/germany")
def germany():
    return render_template("sub/germany.html", title="Germany - ")


@app.route("/australia")
def australia():
    return render_template("sub/australia.html", title="Australia - ")


@app.route("/ksa")
def ksa():
    return render_template("sub/ksa.html", title="KSA - ")


@app.route("/netherlands")
def netherlands():
    return render_template("sub/netherlands.html", title="Netherlands - ")


#  Destinations | Services | Contact

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=3000, debug=True)
    app.run()
