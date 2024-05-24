import requests
import pandas as pd
headers_1 = {"x-zomato-api-key": "put Your api key here"} #api key header

base_url = "http://weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id=" #base link for fetching data using locality id
local_id = "ZWL003915" ## Enter you local Id ##
complete_url = base_url + local_id # complete url
response = requests.get(complete_url, headers=headers_1) # using the response function
if(response.status_code == 200):
    print('Data Fetched')
    y = response.json() #making object of the fetched data

    parsed_data = y["locality_weather_data"]
    df = pd.DataFrame(parsed_data, index=['metrics']) ## Converting the fetched data into Pandas Dataframe

    print(df) # Printing the Pandas Dataframe
else:
    print('Error in fetching data')
    

