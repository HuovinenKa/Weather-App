import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]

        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        wind_speed = wind["speed"]

        weather_info = (
            f"City: {city}\n"
            f"Temperature: {temperature}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Description: {description}\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        return weather_info
    else:
        return "City Not Found"

def main():
    api_key = "1ab43bda6c8fec81a4552e949b28969e"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    weather_info = get_weather(api_key, city)
    print(weather_info)

if __name__ == "__main__":
    main()