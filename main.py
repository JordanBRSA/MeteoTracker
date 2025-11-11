from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/meteo/<string:ville>")
def meteo(ville : str):
    return render_template("meteo.html", ville=ville)






