from city_details import current_city
from services.weather import get_weather
from services.covid_updater import construct_message
from services.telegram import send_telegram_message
from services.air_quality import get_air_quality
 
city = current_city['name']
lat = current_city['lat']
lon = current_city['lon']

base_message = f'{construct_message()}\n{get_weather(city)}\n\n{get_air_quality(lat, lon)}'

send_telegram_message(base_message)
