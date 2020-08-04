## Version History

![PyPI](https://img.shields.io/pypi/v/cli-weather?color=blue&label=PyPI&logo=python&logoColor=yellow&style=plastic)

4 - Beta Limited Use Release
- Introduced new feature to support airquality forecast for next 3 days with 12 hours intervals when used in conjunction with -a and -f which stands for --airquality and --forecast respectively.
- Able to provide key data like aqi and its associated category,concentration of surface no2,so2,co and concentration of particulate matters.
- Introduced --version and --about to provide the version of PyPI package and description of the project.
- Almost production ready, if General API is upgraded since it does not server more than 1 simultaneous HTTPS response.

![PyPI](https://img.shields.io/badge/PyPI-v0.1.4-blue?style=plastic&logo=python&logoColor=yellow)

3 - Alpha Test Release
- Introduced new optional argument -f, --forecast which gives 7 day weather forecast [for now will extend to airquality forecast by next release] with daily intervals from any point on the planet. The result can be fetched by either the city name or postalcode.
- Forecast data from the world's most accurate weather models including the GFS 13km, ECMWF, DWD 6.5km ICON-Europe, and NOAA 3km HRRR.
- Code reuse made for both city and postalcode by dividing functions in each class to new modules altogether.

![PyPI](https://img.shields.io/badge/PyPI-v0.1.3-blue?style=plastic&logo=python&logoColor=yellow)

3 - Alpha Test Release
- Current Air quality observations for any point in the world.Returns current information on the six major pollutants - PM 2.5, PM 10, CO, SO2, NO2, and O3 as well as an US EPA AirQuality Index (AQI) score.
- Detailed aqi information along with its associated category and subsequent health risk status.
- Functional-Programming layout, scope for more by next release
- Set choices for units to avoid wrong units chosen
- Change in description of --detailed optional argument to accomodate new -a functionality
- Choose a subparser status during empty positional argument scenario

![PyPI](https://img.shields.io/badge/PyPI-v0.1.2-blue?style=plastic&logo=python&logoColor=yellow)

3 - Alpha Test Release
- Python2 and Python3 compatible
- Introduction of wheel distribution in binary
- Minor bug fixes in setup.py

![PyPI](https://img.shields.io/badge/PyPI-v0.1.1-blue?style=plastic&logo=python&logoColor=yellow)

3 - Alpha Test Release
- Minor bug fixes in setup.py
- Doc update in PyPIDocumentation.md

![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue?style=plastic&logo=python&logoColor=yellow)

3 - Alpha Test Release
- Get weather by city
- Get weather by postalcode
- Change units according as you wish [Metric/Scientific/Farenheit]
- Only temparature by default, detailed information from snowfall to solar radiation using -d
