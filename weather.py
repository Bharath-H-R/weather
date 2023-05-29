"""
# import required modules
import requests, json

# Enter your API key here
api_key = "249e00fc0a96e388e251c0a51e0cdf0f"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

	# store the value of "main"
	# key in variable y
	y = x["main"]

	# store the value corresponding
	# to the "temp" key of y
	current_temperature = y["temp"]

	# store the value corresponding
	# to the "pressure" key of y
	current_pressure = y["pressure"]

	# store the value corresponding
	# to the "humidity" key of y
	current_humidity = y["humidity"]

	# store the value of "weather"
	# key in variable z
	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]

	# print following values
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description))

else:
	print(" City Not Found ")


"""

import requests
import json

API_KEY = '249e00fc0a96e388e251c0a51e0cdf0f'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_forecast(city):
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return f"The current weather in {city} is {temperature}°C with {description}."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
    except (KeyError, IndexError) as e:
        return f"Error: Failed to parse weather data. {str(e)}"

city = input("Enter a city name: ")
forecast = get_weather_forecast(city)
print(forecast)
