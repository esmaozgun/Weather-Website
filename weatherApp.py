import requests

def get_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
    response = requests.get(url)
    return response.json()

def display_weather_info(weather_data, city):
    if weather_data['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_data['weather'][0]['main']
        fahrenheit = round(weather_data['main']['temp'])
        wind_speed = weather_data['wind']['speed']
        wind_direction = weather_data['wind']['deg']
        temp = convert_to_celc(fahrenheit)

        print(f"The weather in {city} is: {weather}")
        print(f"The temperature in {city} is: {temp}ºC")
        print(f"The wind speed in {city} is: {wind_speed} mph")
        print(f"The wind direction in {city} is: {wind_direction}°")

def convert_to_celc(value):
    #print(value) 
    return (value - 32 ) / (1.8) 


def main():
    api_key = '4814f46b75980f6cfe8d0c3e1108ee27'

    while True:
        user_input = input("Enter a city (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Exiting program...")
            break
        
        weather_data = get_weather_data(user_input, api_key)
        display_weather_info(weather_data, user_input)

if __name__ == "__main__":
    main()