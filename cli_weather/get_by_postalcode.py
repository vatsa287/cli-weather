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
        "-a","--airquality",
        action="store_true",
        help="current air quality observations"
    )
    postalcode_parser.add_argument(
        "-d","--detailed",
        help="display sdetailed weather data",
        action="store_true"
    )
    postalcode_parser.add_argument(
        "-c", "--country",
        help="country of entered area",
        default=""
    )
    postalcode_parser.add_argument(
        "-u", "--units",
        choices=['M','S','F'],
        help="M - [DEFAULT] Metric (Celcius, m/s, mm)\nS - Scientific (Kelvin, m/s, mm)\nI - Fahrenheit (F, mph, in)",
        default="M"
    )

def postalcode_parse(args):
    postalcode = args.postalcode
    country = "&" + args.country
    units = args.units
    API_KEY = "2a7db0585e7541018229c17efb2efa94"

    if args.airquality is True:
        if args.country == "":
            API_URL = "https://api.weatherbit.io/v2.0/current/airquality?postal_code="+postalcode+"&key="
        else:
            API_URL = "https://api.weatherbit.io/v2.0/current/airquality?postal_code="+postalcode+country+"&key="
    elif args.airquality is False:
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
        print("Please use format ex: $ cli-weather postal-code 560032 [-c country_name][-a][-u M/S/F][-d]")
        return

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

    # call arguments based on selected combination of optional arguments
    if args.detailed is False and args.airquality is False:
        get_basic_temparature(main_data, degree)

    elif args.detailed is True and args.airquality is False:
        get_detailed_weather(main_data, degree, speed, distance)

    elif args.detailed is False and args.airquality is True:
        get_basic_airquality(main_data)

    elif args.detailed is True and args.airquality is True:
        get_detailed_airquality(main_data)

def get_basic_temparature(main_data, degree):
    data = main_data['data']
    city = data[0]['city_name']
    print("Current temparature in {} is {} {}" .format(city.capitalize(), data[0]['temp'], degree))

def get_detailed_weather(main_data, degree, speed, distance):
    data = main_data['data']
    city = data[0]['city_name']
    weather = data[0]['weather']
    print("Displaying current weather data.Have a nice day!\n")
    print("city                     : {}".format(data[0]['city_name']))
    print("temparature              : {} {}".format(data[0]['temp'], degree))
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
    print("wind speed               : {} {}".format(data[0]['wind_spd'], speed))
    print("wind direction           : {} degrees".format(data[0]['wind_dir']))
    print("visibility               : {} KM".format(data[0]['vis']))
    print("relative humidity        : {} %".format(data[0]['rh']))
    print("snowfall                 : {} {}/hr".format(data[0]['snow'], distance))
    print("estimated solar radiation: {} W/m^2".format(data[0]['solar_rad']))

def calculate_aqi_category(aqi):
    if aqi <= 50:
        return "GOOD"
    elif aqi > 50 and aqi <= 100:
        return "SATISFACTORY"
    elif aqi > 100 and aqi <= 200:
        return "MODERATE"
    elif aqi > 200 and aqi <= 300:
        return "POOR"
    elif aqi > 300 and aqi <= 400:
        return "VERY POOR"
    elif aqi > 400 and aqi <= 500:
        return "SEVERE"

def get_aqi_risk_status(aqi_category):
    if aqi_category == "GOOD":
        return "There is little or no health risk associated with air quality"
    elif aqi_category == "SATISFACTORY":
        return "Acceptable air quality, but some people who are sensitive to pollution or experience breathing issues may experience adverse effects,\ndepending on the type of contaminants in the air."
    elif aqi_category == "MODERATE":
        return "There is a health risk for children, older adults and people with heart disease and lung disease.\nThe general healthy population isn't likely to experience health risks."
    elif aqi_category == "POOR":
        return "Considered unsafe and anyone could experience negative health effects from pollution in the air."
    elif aqi_category == "VERY POOR":
        return "Serious health risk level for everyone and is in best interest to stay indoors or leave the area wearing N95 masks."
    elif aqi_category == "SEVERE":
        return "Considered hazardous and it's likely causes are accidental nuclear spill or harmful gases. Evacuate immediately gas suits are recommended.\nLikely that emergency is declared in this area."

def get_basic_airquality(main_data):
    data = main_data['data']
    aqi = data[0]['aqi']
    aqi_category = calculate_aqi_category(aqi)
    aqi_risk_status = get_aqi_risk_status(aqi_category)
    print("Current AQI(Air Quality Index) in {} is {} and falls under '{}' category according to Central Pollution Control Board".format(main_data['city_name'],aqi,aqi_category))
    print("\nHealth Risk Status:")
    print(aqi_risk_status)

def get_detailed_airquality(main_data):
    data = main_data['data']
    aqi = data[0]['aqi']
    aqi_category = calculate_aqi_category(aqi)
    aqi_risk_status = get_aqi_risk_status(aqi_category)
    print("Displaying current Air Quality data.Have a nice day!\n")
    print("city                                                  : {}".format(main_data['city_name']))
    print("timezone                                              : {}".format(main_data['timezone']))
    print("air-quality-index                                     : {}".format(aqi))
    print("concentration of surface o3(ozone)                    : {} {}".format(data[0]['o3'],"µg/m³"))
    print("concentration of surface so2(sulphur dioxide)         : {} {}".format(data[0]['so2'],"µg/m³"))
    print("concentration of surface co(carbon monooxide)         : {} {}".format(data[0]['so2'],"µg/m³"))
    print("concentration of surface no2(nitrogen dioxide)        : {} {}".format(data[0]['so2'],"µg/m³"))
    print("concentration of particulate matter<10 microns(pm10)  : {} {}".format(data[0]['pm10'],"µg/m³"))
    print("concentration of particulate matter<2.5 microns(pm2.5): {} {}".format(data[0]['pm25'],"µg/m³"))

    print("\nAQI category as per central pollution control board   : {}".format(aqi_category))

    print("\nHealth Risk Status:")
    print(aqi_risk_status)

    print("\nAir-Quality-Index and Category standard set by CPCB\n")

    print("-------------------------------------------------------")
    print("|aqi               |category                          |")
    print("-------------------------------------------------------")
    print("'0-50              'good                              '")
    print("'51-100            'satisfactory                      '")
    print("'101-200           'moderate                          '")
    print("'201-300           'poor                              '")
    print("'301-400           'very poor                         '")
    print("'401-500           'severe                            '")
    print("-------------------------------------------------------")

    #Introduced airquality,functional-programming,set choices for units,try-execpt order m/s/f,change detailed help desc