import requests

API_KEY = 'YOUR_API_KEY'  # Replace with your actual key
BASE_URL = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None

def print_weather(data):
    if data and data.get('main'):
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print("No weather data found.")

def main():
    city = input("Enter city name: ")
    data = get_weather(city)
    print_weather(data)

if __name__ == "__main__":
    main()