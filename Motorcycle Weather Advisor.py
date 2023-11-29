import requests
from dateutil import parser


data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,precipitation,wind_speed_10m,wind_gusts_10m&forecast_days=3")

data = data.json()["hourly"]

weather_list = []
for i in range(len(data['time'])):
    weather_dict = {
        'time': parser.parse(data['time'][i]),
        'temperature': data['temperature_2m'][i],
        'precipitation': data['precipitation'][i] * 100,
        'wind_speed': data['wind_speed_10m'][i],
        'wind_gusts': data['wind_gusts_10m'][i]
    }
    weather_list.append(weather_dict)

relevant_blocks = []

for x in weather_list:
    if x["time"].hour == 8:
       relevant_blocks.append(x)

print(relevant_blocks)

for day in relevant_blocks:
    if day["temperature"] < 5 or day["precipitation"] > 75 or day["wind_speed"] > 40 or day["wind_gusts"] > 40:
        print(day["time"], " - Dont ride today")
    else:
        print(day["time"], " - Fine to ride today")
