from flask import Flask, render_template, request
from weather import get_weather

app = Flask(__name__)

API_KEY = "57c4d0ef3cebaf6d9b98ff3ed5a7fb40"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        
        if not city:
            error = "Please enter a city name."
        else:
            data = get_weather(city, API_KEY)

            if "main" not in data:
                error = "City not found. Try again!"
            else:
                weather_data = {
                    "city": city,
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "desc": data["weather"][0]["description"].title()
                }

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
