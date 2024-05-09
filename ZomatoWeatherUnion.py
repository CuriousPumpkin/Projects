import requests
headers_1 = {"x-zomato-api-key": "e6ad65a43babf3552af8a84fa44ca0a4"}

base_url = "http://weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id="
local_id = "ZWL004722"
complete_url = base_url + local_id
response = requests.get(complete_url, headers=headers_1)
if(response.status_code == 200):
    print('Data Fetched')
else:
    print('Error in fetching data')
    

y = response.json()
temperature = y['locality_weather_data']["temperature"]
humidity = y['locality_weather_data']["humidity"]
wind_speed = y['locality_weather_data']["wind_speed"]
wind_direction = y['locality_weather_data']["wind_direction"]
rain_intensity = y['locality_weather_data']["rain_intensity"]
rain_accumulation = y['locality_weather_data']["rain_accumulation"]


print(y["locality_weather_data"])