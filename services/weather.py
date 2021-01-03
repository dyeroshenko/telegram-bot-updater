# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime

def kelvin_to_celsius(temp):
        transformed = str(int(round(temp - 273.15, 0))) + '°C'
        return transformed

def get_weather(city):

    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":{city}}


    headers = {
        'x-rapidapi-key': "###YOUR API KEY###",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    weather = data['weather']
    description = weather[0]['description']

    temp = data['main']
    
    current_temp = temp['temp']
    min_temp = temp['temp_min']
    max_temp = temp['temp_max']
    feels_like = temp['feels_like']

    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')

    message = f"Today in Wroclaw is: *{description}*\nCurrent temperature: *{kelvin_to_celsius(current_temp)}* and feels like {kelvin_to_celsius(feels_like)}\nLow: {kelvin_to_celsius(min_temp)} and high: {kelvin_to_celsius(max_temp)}\nSunset at {sunset}"
    
    return message 


