from __future__ import print_function
from datetime import datetime

def timestamp_to_datetime(timestamp):
    """
    Convert the date object from timestamp format
    to date-time format
    """
    date_object = datetime.fromtimestamp(timestamp)
    date = str(date_object)
    date = date.split(" ")
    # return only the time
    return date[1]

# return time in string format
def timestamp_to_strftime(timestamp):
    """
    Convert time in timestamp format 
    to string format
    """
    date_object = datetime.fromtimestamp(timestamp)
    date = date_object.strftime("%d %B, %Y")
    return(date)

"""
    Calculate aqi category from given aqi
"""
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

def get_airquality_forecast(main_data):
    # start with day day hour day, skip 12 hours for every iteration
    day = 0
    data = main_data['data']

    print("Air-uality forecast for next 3 days with 12 hours interval. Have a nice time!\n")

    print("------------------------------------------------------------------------\n")

    print("city                     : {}".format(main_data['city_name']))
    print("timezone                 : {}\n".format(main_data['timezone']))

    print("------------------------------------------------------------------------\n")

    while(day < 72):
        aqi = data[day]['aqi']
        aqi_category = calculate_aqi_category(aqi)
        print("date                                                  : {}".format(timestamp_to_strftime(data[day]['ts'])))
        print("time                                                  : {}".format(timestamp_to_datetime(data[day]['ts'])))
        print("air-quality-index                                     : {}".format(aqi))
        print("concentration of surface o3(ozone)                    : {} {}".format(data[day]['o3'],"µg/m³"))
        print("concentration of surface so2(sulphur dioxide)         : {} {}".format(data[day]['so2'],"µg/m³"))
        print("concentration of surface co(carbon monooxide)         : {} {}".format(data[day]['so2'],"µg/m³"))
        print("concentration of surface no2(nitrogen dioxide)        : {} {}".format(data[day]['so2'],"µg/m³"))
        print("concentration of particulate matter<10 microns(pm10)  : {} {}".format(data[day]['pm10'],"µg/m³"))
        print("concentration of particulate matter<2.5 microns(pm2.5): {} {}".format(data[day]['pm25'],"µg/m³"))

        print("\nAQI category as per central pollution control board   : {}\n".format(aqi_category))

        print("------------------------------------------------------------------------\n")
        day+=12
