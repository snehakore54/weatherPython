import requests

def get_weather(city_name):
    api_key = "b7b8f5bcb419430e893134256240510"  
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}"

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        
        weather_data = response.json()
        
        location = weather_data['location']['name']
        temp_c = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        humidity = weather_data['current']['humidity']
        wind_kph = weather_data['current']['wind_kph']
        
        print(f"Weather in {location}:")
        print(f"Temperature: {temp_c}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_kph} kph")
        
    except requests.exceptions.RequestException as error:
        print(f"Error on fetching the weather data: {error}")

city = "Hyderabad"
get_weather(city)
