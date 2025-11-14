from flask import Flask, render_template , request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ville = request.form.get("ville")  # récupère la ville du formulaire
        if ville:
            return redirect(url_for("meteo", ville=ville))  # redirige vers /meteo/<ville>
    return render_template("index.html")


@app.route("/meteo/<string:ville>")
def meteo(ville : str):
    return render_template("meteo.html", ville=ville)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)








