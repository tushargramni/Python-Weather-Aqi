from math import degrees

import requests

api_key = "3c71d6698143fea43a4df6f44e5575f0"
lat = ""
lon = ""
def Current_Weather_DataAPI():
    city_name = input("Enter the city name: ")
    params = {"q": city_name,
              "appid": api_key,
              "units": "metric"
              }
    url = f"https://api.openweathermap.org/data/2.5/weather"

    response = requests.get(url, params=params)

    if response.status_code != 200:
        error_msg = response.json().get("message", "Something went wrong")
        print(f"Error ({response.status_code}): {error_msg}")
        return False

        # print(response.json())
    data = response.json()

    for weather in data['weather']:
        print("Description: ",(weather['description']))
    # print("Weather Description: ", response.json()['weather'][0]['description'])

    for key, value in data['main'].items():
        if key == 'temp':
            print(f"Temperature: {value}°C")
    # print("Temperature: ", response.json()['main']['temp'])

    for key,value in data['coord'].items():
        if key == 'lon':
            global lon
            lon = value
            print(f"Longitude: {value}")
        if key == 'lat':
            global lat
            lat = value
            print(f"Latitude: {value}")
    # print(f"{city_name} Coordinates: ", response.json()['coord']['lon'])
    # print(f"{city_name} Coordinates: ", response.json()['coord']['lat'])

Current_Weather_DataAPI()

def Air_Pollution_API():
    # longitude = input("Enter Longitude: ")
    # latitude = input("Enter Latitude: ")
    params = {
        'lat' : lat,
        'lon' : lon,
        'appid': api_key
    }
    url = f"https://api.openweathermap.org/data/2.5/air_pollution"
    data = requests.get(url,params=params)
    if data.status_code != 200:
        error_msg = data.json().get("message", "Something went wrong")
        print(f"Error ({data.status_code}): {error_msg}")
        return False

    air_quality= data.json()['list'][0];
    print(f"Air Quality(AQI): {air_quality['main']['aqi']}")
    print(f"Components: ")
    for key,value in air_quality['components'].items():
        print(f"{key}: {value}")

Air_Pollution_API()




