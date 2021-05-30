from __future__ import print_function
import requests
import argparse

# handle ModuleNotFoundError during python3 execution
try:
    from cli_weather.airquality_data import *
    from cli_weather.weather_data import *
    from cli_weather.weather_forecast_data import *
    from cli_weather.airquality_forecast_data import *
except ModuleNotFoundError:
    from airquality_data import *
    from weather_data import *
    from weather_forecast_data import *
    from airquality_forecast_data import *

def get_by_city_args(subparsers):
    """
    add positinal argument 'city' to argparser
    """
    city_parser = subparsers.add_parser('city',
        formatter_class=argparse.RawTextHelpFormatter
    )
    city_parser.add_argument(
        "city",
        help="get weather by city name"
    )
    city_parser.add_argument(
        "-a","--airquality",
        action="store_true",
        help="current air quality observations"
    )
    city_parser.add_argument(
        "-d","--detailed",
        help="display detailed data [not applicable for forecast]",
        action="store_true"
    )
    city_parser.add_argument(
        "-f","--forecast",
        action="store_true",
        help="forecast on weather or airquality"
    )
    city_parser.add_argument(
        "-c", "--country",
        help="country of entered area",
        default=""
    )
    city_parser.add_argument(
        "-u", "--units",
        choices=['M','S','I'],
        help="M - Metric (Celcius, m/s, mm) [DEFAULT]\nS - Scientific (Kelvin, m/s, mm)\nI - Imperial (F, mph, in)",
        default="M"
    )


def city_parse(args):
    """
    Send API request to WeatherBIT for city based input
    and call respective methods based on optional arguments
    """
    city = args.city
    country = "&" + args.country
    units = args.units
    API_KEY = "2a7db0585e7541018229c17efb2efa94"


    if args.airquality is True and args.forecast is False:
        if args.country == "":
            API_URL = "https://api.weatherbit.io/v2.0/current/airquality?city="+city+"&key="
        else:
            API_URL = "https://api.weatherbit.io/v2.0/current/airquality?city="+city+country+"&key="

    elif args.airquality is False and args.forecast is True:
        if args.country == "":
            API_URL = "https://api.weatherbit.io/v2.0/forecast/daily?city="+city+"&key="
        else:
            API_URL = "https://api.weatherbit.io/v2.0/forecast/daily?city="+city+country+"&key="

    elif args.airquality is True and args.forecast is True:
         if args.country == "":
            API_URL = "https://api.weatherbit.io/v2.0/forecast/airquality?city="+city+"&key="
         else:
            API_URL = "https://api.weatherbit.io/v2.0/forecast/airquality?city="+city+country+"&key="

    elif args.airquality is False:
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

    try:
        main_data = response.json()
    # ValueError-unable to decode json, UnboundLocalError-used var before declaring
    except (ValueError,UnboundLocalError) as err:
        print("Invalid city")
        print("Please use format ex: $ cli-weather bengaluru [-c country_name][-a][-u M/S/F][-d]")
        return

    # defalut metric values
    degree = "celcius"
    speed = "m/s"
    distance = "mm"

    if args.units == "S":
        degree = "kelvin"
    elif args.units == "I":
        degree = "Fahrenheit"
        speed = "mph"
        distance = "in"

    choice = [True, False]
    if args.airquality is False and args.detailed in choice and args.forecast is True:
        get_weather_forecast(main_data, degree, speed, distance)
        return
    elif args.airquality is True and args.detailed in choice and args.forecast is True:
        get_airquality_forecast(main_data)
        return

    # call respective methods based on selected combination of optional arguments in cli-weather
    if args.detailed is False and args.airquality is False:
        get_basic_temparature(main_data, degree)

    elif args.detailed is True and args.airquality is False:
        get_detailed_weather(main_data, degree, speed, distance)

    elif args.detailed is False and args.airquality is True:
        get_basic_airquality(main_data)

    elif args.detailed is True and args.airquality is True:
        get_detailed_airquality(main_data)
