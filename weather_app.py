import requests
import json

# Asking user to save weather information into json file
def saveWeather(data):
    save = input("\nWould you like to save the weather information? y/n? ")
    if save == 'y':
        with open('savedWeather.json', 'w') as new_file:
            json.dump(data, new_file, indent=4)
            print("Weather infromation saved to: savedWeather.json")
    else:
        print("Not saved")

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(response)
        return None


# Main
if __name__ == "__main__":
    api_key = "1ab43bda6c8fec81a4552e949b28969e"
    city = input("Enter the city name: ")
    weather_data = get_weather(api_key, city)
    
    if weather_data:
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")

        # Asking user to save weather information
        saveWeather(weather_data)
    else:
        print("Error fetching the weather data.")
