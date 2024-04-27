import requests
import json 
from config import api_key # Use your own API Key

def get_weather_data(lat, lon):
    # Construct the API request URL 
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    
    # Send an HTTP GET request to the API 
    response = requests.get(url, params={'units': 'metric',})

    # Check if response was successful
    if response.status_code == 200:
        # Parse JSON data returned by API 
        data = json.loads(response.text)

        # Extract relevant weather data from data variable
        weather_data = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"]
        }

        return weather_data
    
    else: 
        print("Error: ", response.status_code)
        return None
    

def get_geocode(location):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={api_key}" # limit can be any number but is now set to 5 
    
    response = requests.get(url)

    # Check if response was successful
    if response.status_code == 200:
        # Parse JSON data returned by API 
        data = json.loads(response.text)

        # Obtain lat and lon info for get_weather_data url 
        geo_data = {
            "lat": data[0]["lat"],
            "lon": data[0]["lon"],
        }

        return geo_data

    else: 
        print("Error: ", response.status_code)
        return None


def main():
    # Ask user for a location
    location = input("Enter a location (e.g. New York, London): ")

    geo_data = get_geocode(location)
    lat = geo_data["lat"]
    lon = geo_data["lon"]

    # Retrieve data with get_weather function  
    weather_data = get_weather_data(lat, lon)

    if weather_data:
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Weather Description: {weather_data['weather_description']}")

if __name__ == "__main__":
    main()



        