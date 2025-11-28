from flask import Flask, render_template, request
from utils.weather import get_weather

API_KEY = "57c4d0ef3cebaf6d9b98ff3ed5a7fb40"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        data = get_weather(city, API_KEY)

        if "main" in data:
            weather_data = {
                "city": city,
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "desc": data["weather"][0]["description"]
            }
        else:
            error = "City not found! Try another city."

    return render_template("index.html", weather_data=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
