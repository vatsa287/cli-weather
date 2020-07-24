import requests
import json
import argparse

def get_by_city_args(subparsers):
    city_parser = subparsers.add_parser('city')
    city_parser.add_argument(
        "city",
        help = "enter city name to get current temparature"
    )
    city_parser.add_argument(
        "-c", "--country",
        help = "country of the city",
        default=""
    )
    city_parser.add_argument(
        "-u", "--units",
        help = "M - [DEFAULT] Metric (Celcius, m/s, mm), S - Scientific (Kelvin, m/s, mm),I - Fahrenheit (F, mph, in)",
        default="M"
    )

def city_parse(args):
    city = args.city
    country = "&" + args.country
    units = args.units
    API_KEY = "2a7db0585e7541018229c17efb2efa94"

    if args.country == "":
        API_URL = "https://api.weatherbit.io/v2.0/current?city="+city+"&key="
    else:
        API_URL = "https://api.weatherbit.io/v2.0/current?city="+city+country+"&key="

    url = API_URL + API_KEY

    querystring = {
        "lang":"en",
        "units":units
        }

    response = requests.request("GET", url, params=querystring)

    main_data = response.json()
    data = main_data['data']

    degree = "celcius"
    if args.units == "S":
        degree = "kelvin"
    elif args.units == "F":
        degree = "Fahrenheit"

    print("Current temparature in {} is {} {}" .format(city.capitalize(), data[0]['temp'], degree))