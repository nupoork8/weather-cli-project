from flask import Flask, render_template, request
from utils.weather import get_weather

app = Flask(__name__, template_folder="templates", static_folder="static")

API_KEY = "57c4d0ef3cebaf6d9b98ff3ed5a7fb40"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            data = get_weather(city, API_KEY)

            if data.get("cod") != 200:
                error = data.get("message", "Something went wrong!")
            else:
                weather_data = {
                    "city": city,
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "desc": data["weather"][0]["description"]
                }

    return render_template("index.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
