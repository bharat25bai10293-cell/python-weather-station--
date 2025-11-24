import requests
import json
import sys 
API_KEY = "b22d993ee030daaa8aa534f2f30593e8" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?" 

def get_weather(city_name):
    """Fetches and displays current weather data for the specified city."""
    
    complete_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units=metric"

    print(f"\n--- Checking weather for {city_name.capitalize()}... ---")

    try:
        response = requests.get(complete_url)
        if response.status_code == 200:
            data = response.json()
            main_data = data.get('main', {})
            weather_list = data.get('weather', [{}])
            temperature = main_data.get('temp', 'N/A')
            humidity = main_data.get('humidity', 'N/A')
            description = weather_list[0].get('description', 'No description')
            print("Data Retrieval Successful")
            print("---------------------------")
            print(f"City: **{data.get('name', city_name.capitalize())}**")
            print(f"Temperature: **{temperature}°C**")
            print(f"Humidity: **{humidity}%**")
            print(f"Conditions: **{description.capitalize()}**")
            print("---------------------------")
            
        elif response.status_code == 404:
            print(f"Error 404: City '{city_name}' not found. Please check spelling.")
        elif response.status_code == 401:
            print("Error 401: Unauthorized. Please check if your API key is correct and fully activated.")
        else:
            print(f"An unexpected API error occurred (Status Code: {response.status_code}).")

    except requests.exceptions.RequestException as e:
        print(f"Network Error: Could not connect to the API. Check your internet connection.")
    except json.JSONDecodeError:
        print("Data Error: Failed to parse the weather data.")


if __name__ == "__main__":
    
   

    city_input_raw = input("Enter city name (e.g., Meerut, London): ")
    
    
    clean_city_name = city_input_raw.strip().strip('"').strip("'")
    
    if clean_city_name:
        get_weather(clean_city_name)
    else:

        print("City name cannot be empty. Exiting.")
