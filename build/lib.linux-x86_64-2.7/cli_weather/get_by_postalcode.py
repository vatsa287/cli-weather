from __future__ import print_function
import requests
import argparse

def get_by_postalcode_args(subparsers):
    postalcode_parser = subparsers.add_parser('postalcode',
        formatter_class=argparse.RawTextHelpFormatter
    )
    postalcode_parser.add_argument(
        "postalcode",
        help="get weather by postal code"
    )
    postalcode_parser.add_argument(
        "-c", "--country",
        help="country of entered area",
        default=""
    )
    postalcode_parser.add_argument(
        "-u", "--units",
        help="M - [DEFAULT] Metric (Celcius, m/s, mm)\nS - Scientific (Kelvin, m/s, mm)\nI - Fahrenheit (F, mph, in)",
        default="M"
    )
    postalcode_parser.add_argument(
        "-d","--detailed",
        help="display sdetailed weather data",
        action="store_true"
    )

def postalcode_parse(args):
    postalcode = args.postalcode
    country = "&" + args.country
    units = args.units
    API_KEY = "2a7db0585e7541018229c17efb2efa94"

    if args.country == "":
        API_URL = "https://api.weatherbit.io/v2.0/current?postal_code="+postalcode+"&key="
    else:
        API_URL = "https://api.weatherbit.io/v2.0/current?postal_code="+postalcode+country+"&key="

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
        print("Invalid postal-code")
        print("Please use format ex: $ cli-weather postal-code 560032 [-c country_name][-u S/M/F][-d]")
        return

    data = main_data['data']
    weather = data[0]['weather']
    # defalut metric values
    degree = "celcius"
    speed = "m/s"
    distance = "mm"

    if args.units == "S":
        degree = "kelvin"
    elif args.units == "F":
        degree = "Fahrenheit"
        speed = "mph"
        distance = "in"

    if args.detailed:
        print("Have a nice day!\n")
        print("city                     : {}".format(data[0]['city_name'].capitalize()))
        print("temparature              : {} {}".format(data[0]['temp'],degree))
        print("summary                  : {}".format(weather['description']))
        print("source station ID        : {}".format(data[0]['station']))
        print("latitude                 : {} degrees".format(data[0]['lat']))
        print("longitude                : {} degrees".format(data[0]['lon']))
        print("timezone                 : {}".format(data[0]['timezone']))
        print("last observation time    : {}".format(data[0]['ob_time']))
        print("sunrise                  : {}".format(data[0]['sunrise']))
        print("sunset                   : {}".format(data[0]['sunset']))
        print("pressure                 : {} mb".format(data[0]['pres']))
        print("sea level pressure       : {} mb".format(data[0]['slp']))
        print("wind speed               : {} {}".format(data[0]['wind_spd'],speed))
        print("wind direction           : {} degrees".format(data[0]['wind_dir']))
        print("visibility               : {} KM".format(data[0]['vis']))
        print("relative humidity        : {} %".format(data[0]['rh']))
        print("snowfall                 : {} {}/hr".format(data[0]['snow'],distance))
        print("estimated solar radiation: {} W/m^2".format(data[0]['solar_rad']))
    elif args.detailed is False:
        print("Current temparature in {} is {} {}" .format(data[0]['city_name'].capitalize(), data[0]['temp'], degree))
    