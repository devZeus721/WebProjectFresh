import requests

def get_weather(city):
    url = f'https://wttr.in/{city}?format=3'  # Simple one-line weather summary
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Weather in {city}: {response.text}")
    except requests.RequestException as e:
        print("Error fetching weather data:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
