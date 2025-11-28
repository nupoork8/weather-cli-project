import os
from flask import Flask, render_template, request
from utils.weather import get_weather

API_KEY = "57c4d0ef3cebaf6d9b98ff3ed5a7fb40"

# Debug: Print the current working directory and paths
print("Current working directory:", os.getcwd())
print("App file location:", os.path.abspath(__file__))

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
print("Template directory:", template_dir)
print("Template directory exists:", os.path.exists(template_dir))

# Check if index.html exists
index_path = os.path.join(template_dir, 'index.html')
print("index.html path:", index_path)
print("index.html exists:", os.path.exists(index_path))

app = Flask(__name__, template_folder=template_dir, static_folder="static")

@app.route("/", methods=["GET", "POST"])
def home():
    print("Home route accessed")
    weather_data = None
    error = None

    if request.method == "POST":
        print("POST request received")
        city = request.form.get("city")
        print(f"City requested: {city}")
        data = get_weather(city, API_KEY)
        print(f"Weather data received: {data}")

        if "main" in data:
            weather_data = {
                "city": city,
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "desc": data["weather"][0]["description"]
            }
            print(f"Weather data processed: {weather_data}")
        else:
            error = "City not found! Try another city."
            print(f"Error: {error}")

    print("About to render template...")
    return render_template("index.html", weather_data=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)