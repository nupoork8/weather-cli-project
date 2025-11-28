import requests
import sys

def get_weather(city,api_key):
    # To get weather, I need two things:
    # 1. The API link
    # 2. The city name + my API key

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q' : city,
        'appid' : api_key,
        'units' : 'metric'
    }

    response = requests.get(url, params=params, timeout = 10)
    return response.json()
    
    

    
def main():
    #handle the incorrect inputs
    #what if user dose'nt give a city ? then show msg & exit

    if len(sys.argv) < 2:
        print("Please Enter a City name !!")
        sys.exit()

    city = sys.argv[1]
    api_key = "57c4d0ef3cebaf6d9b98ff3ed5a7fb40"

    data = get_weather(city, api_key)   

    # Handle API errors
    if "main" not in data:
        print("\n Error:", data.get("message", "Unknown error"))
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {desc}")


if __name__ == "__main__":
    main()   