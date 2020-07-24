import requests
import json
import argparse

parser = argparse.ArgumentParser('cli-weather')
parser.add_argument(
    "city",
    help = "enter city to get current temparature"
)
args = parser.parse_args()

city = args.city

API_KEY = "2a7db0585e7541018229c17efb2efa94"
API_URL = "https://api.weatherbit.io/v2.0/current?city="+city+"&key="

url = API_URL + API_KEY

querystring = {
    "lang":"en",
    "lon":"<required>",
    "lat":"<required>"
    }

response = requests.request("GET", url, params=querystring)

main_data = response.json()
data = main_data['data']

print("Current temparature in {} is {} " .format(city.capitalize(), data[0]['temp']))