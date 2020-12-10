from __future__ import print_function

def get_basic_temparature(main_data, degree):
    """
    Print basic temperature data on the terminal
    """
    data = main_data['data']
    city = data[0]['city_name']
    print("Current temparature in {} is {} {}" .format(city.capitalize(), data[0]['temp'], degree))

def get_detailed_weather(main_data, degree, speed, distance):
    data = main_data['data']
    city = data[0]['city_name']
    weather = data[0]['weather']
    print("Displaying current weather data.Have a nice day!\n")
    print("city                     : {}".format(city.capitalize()))
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