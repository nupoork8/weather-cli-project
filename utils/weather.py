import requests
import sys

def get_weather(city, api):
    url = "http://api.openweathermap.org/data/2.5/weather"
    api_key = ""
    params = {
        'q': city,
        'api_id' : api_key,
        'units' : 'metric'
    }    
    response = response.get(url, params = params , timeout = 10)
    return response.json()

def main():
    get_weather("mumbai")