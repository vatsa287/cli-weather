from __future__ import print_function

def calculate_aqi_category(aqi):
    """
    Get the aqi from JSON data of WeatherBIT
    and return the category for which the 
    aqi belongs to
    """
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
    """
    Return health risk status based on to
    which category does air-quality index falls.
    """
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
    """
    Get AQI as JSON input from WeatherBIT API and return
    AQI, which category does it belong to and also associated 
    health risk
    """
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
