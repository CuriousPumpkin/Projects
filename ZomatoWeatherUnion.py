import requests
headers_1 = {"x-zomato-api-key": "Your api key"} #api key header

base_url = "http://weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id=" #base link for fetching data using locality id
local_id = "ZWL003915"
complete_url = base_url + local_id # complete url
response = requests.get(complete_url, headers=headers_1) # using the response function
if(response.status_code == 200):
    print('Data Fetched')
else:
    print('Error in fetching data')
    

y = response.json() #making object of the fetched data
temperature = y['locality_weather_data']["temperature"]
humidity = y['locality_weather_data']["humidity"]
wind_speed = y['locality_weather_data']["wind_speed"]
wind_direction = y['locality_weather_data']["wind_direction"]
rain_intensity = y['locality_weather_data']["rain_intensity"]
rain_accumulation = y['locality_weather_data']["rain_accumulation"]


print(y["locality_weather_data"]) # printing the dictionary of the weather data