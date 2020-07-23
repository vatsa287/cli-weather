import requests
import json

API_KEY = "2a7db0585e7541018229c17efb2efa94"
API_URL = "https://api.weatherbit.io/v2.0/current?city=bengaluru&key="+API_KEY

response = requests.request("GET", API_URL)

main_data = response.json()
data = main_data['data']

print(data[0]['temp'])