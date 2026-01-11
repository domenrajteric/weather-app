# Osnovni Flask paket
from flask import Flask, render_template, request

# Komunikacija/zahtevki med 2 aplikacijama
import requests

# Za dostop do okoljske spremenljivke (environment variable)
import os

app = Flask(__name__)

# Vstopni "HANDLER", ki obravnava tako "GET" kot "POST" zahtevke
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":
        # API klic potrebuje spodnje 3 podatke oz. spremenljivke ...
        city = request.form.get("city")         # Kraj
        unit = "metric"                         # Merska enota: "metric" ali "imperial"
        api_key = os.environ.get("API_KEY")     # API ključ, ki mora ostati "skrit"

        # URL za klic/zahtevek, ki vključuje zgornje 3 informacije
        url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(city, unit, api_key)

        # Klic/zahtevek > povratne informacije shranjene v  spremenljivki "data"
        data = requests.get(url=url)

        # Print v terminal: "print(data.json())" ali v HTML: "<p>{{data}}</p>

        return render_template("index.html", data=data.json())


if __name__ == "__main__":
    app.run()



