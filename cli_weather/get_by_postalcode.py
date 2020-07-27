import requests
import argparse

def get_by_postalcode_args(subparsers):
    postalcode_parser = subparsers.add_parser('postalcode',
        formatter_class=argparse.RawTextHelpFormatter
    )
    postalcode_parser.add_argument(
        "postalcode",
        help="enter postal code to get current temparature"
    )
    postalcode_parser.add_argument(
        "-c", "--country",
        help="country of given postal code",
        default=""
    )
    postalcode_parser.add_argument(
        "-u", "--units",
        help="M - [DEFAULT] Metric (Celcius, m/s, mm)\n\S - Scientific (Kelvin, m/s, mm)\nI - Fahrenheit (F, mph, in)",
        default="M"
    )
    postalcode_parser.add_argument(
        "-d","--detailed",
        help="detailed weather data",
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
        print("Please use format ex: $ cli-weather postal-code 560032 [-c country_name][-u S/M/F] [-d]")
        return

    data = main_data['data']
    weather = data[0]['weather']
    # defalut metric values
    degree = "celcius"
    speed = "m/s"

    if args.units == "S":
        degree = "kelvin"
    elif args.units == "F":
        degree = "Fahrenheit"
        speed = "mph"

    if args.detailed:
        print(
            " Have a nice day!\n\n",
            "city: {}\n".format(data[0]['city_name'].capitalize()),
            "temparature: {} {}\n".format(data[0]['temp'],degree),
            "summary: {}\n".format(weather['description']),
            "source station ID: {}\n".format(data[0]['station']),
            "latitude: {} degrees\n".format(data[0]['lat']),
            "longitude: {} degrees\n".format(data[0]['lon']),
            "timezone: {}\n".format(data[0]['timezone']),
            "last observation time: {}\n".format(data[0]['ob_time']),
            "sunrise: {}\n".format(data[0]['sunrise']),
            "sunset: {}\n".format(data[0]['sunset']),
            "pressure: {} mb\n".format(data[0]['pres']),
            "sea level pressure: {} mb\n".format(data[0]['slp']),
            "wind speed: {} {}\n".format(data[0]['wind_spd'],speed),
            "wind direction: {} degrees\n".format(data[0]['wind_dir']),
            "visibility: {} KM\n".format(data[0]['vis']),
            "relative humidity: {} %\n".format(data[0]['rh']),
            "estimated solar radiation: {} W/m^2".format(data[0]['solar_rad'])
        )
    elif args.detailed is False:
        print("Current temparature in {} is {} {}" .format(data[0]['city_name'].capitalize(), data[0]['temp'], degree))
    