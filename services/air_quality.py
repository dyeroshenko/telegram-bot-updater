import requests

base_url = "https://air-quality.p.rapidapi.com/forecast/airquality"


def get_air_quality(lat,lon):

    querystring = {"lat":{lat},"lon":{lon},"hours":"24"}

    headers = {
        'x-rapidapi-key': "###YOUR API KEY###",
        'x-rapidapi-host': "air-quality.p.rapidapi.com"
        }

    response = requests.request("GET", base_url, headers=headers, params=querystring)

    data = response.json()
    main = data['data']

    strings = []

    for i in main:
        timestamp = i['timestamp_local'][11:][:5]
        aqi = i['aqi']

        if aqi <= 50:
            status = 'Good'
        elif (aqi > 50 and aqi <= 100): 
            status = 'Moderate'
        elif (aqi > 100 and aqi <= 200):
            status = '*Unhealthy*'
        elif (aqi > 200 and aqi <= 300):
            status = '*Very unhealthy*'
        else:
            status = '*Hazardous*'  

        if (timestamp == '08:00'
        or timestamp == '10:00'
        or timestamp == '14:00'
        or timestamp == '18:00'
        or timestamp == '22:00'
        ):
            message =(f'{timestamp}: {status}({aqi})\n')
            strings.append(message)

    message = ('').join(strings)
    return f'*Air quality*:\n{message}'

    