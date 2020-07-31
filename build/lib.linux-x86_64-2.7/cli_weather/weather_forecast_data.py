from __future__ import print_function
from datetime import datetime

def timestamp_to_datetime(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    date = str(date_object)
    date = date.split(" ")
    # return only the time
    return date[1]

# return time in string format
def timestamp_to_strftime(timestamp):
    date_object = datetime.fromtimestamp(timestamp)
    date = date_object.strftime("%d %B, %Y")
    return(date)

def get_weather_forecast(main_data, degree, speed, distance):
    # forecast for next 7 days
    days = 7
    data = main_data['data']

    print("Forecast for next 7 days. Have a nice week!\n")

    print("-----------------------------------------------------\n")

    print("city                     : {}".format(main_data['city_name']))
    print("timezone                 : {}\n".format(main_data['timezone']))

    print("-----------------------------------------------------\n")

    for day in range(0,days+1):
        weather = data[day]['weather']
        print("date                     : {}".format(timestamp_to_strftime(data[day]['sunrise_ts'])))
        print("maximum temparature      : {} {}".format(data[day]['max_temp'], degree))
        print("minimum temparature      : {} {}".format(data[day]['min_temp'], degree))
        print("average temparature      : {} {}".format(data[day]['temp'], degree))
        print("sunrise                  : {}".format(timestamp_to_datetime(data[day]['sunrise_ts'])))
        print("sunset                   : {}".format(timestamp_to_datetime(data[day]['sunset_ts'])))
        print("summary                  : {}".format(weather['description']))
        print("visibility               : {} KM".format(data[day]['vis']))
        print("relative humidity        : {} %".format(data[day]['rh']))
        print("snowfall                 : {} {}/hr\n".format(data[day]['snow'], distance))
        print("-----------------------------------------------------\n")

