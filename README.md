[![BuiltWithPython](https://img.shields.io/badge/Built%20With%20-Python-orange?style=for-the-badge&logo=python&logoColor=green)](https://img.shields.io/badge/Built%20With%20-Python-orange?style=for-the-badge&logo=python?logoColor=green)
# cli-weather  [![Downloads](https://pepy.tech/badge/cli-weather)](https://pepy.tech/project/cli-weather)

<p align="center">
  <img src="https://raw.githubusercontent.com/vatsa287/cli-weather/master/assets/showhelp2.svg?raw=true">
</p>

---

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
  - [Local Installation](#local-installation)  <!-- [Features at a Glance](#features-at-a-glance) -->
  - [Tarball and Wheel Installation](#tarball-and-wheel-installation)
- [Basic Usage](#basic-usage)
  - [Features at a glance](#features-at-a-glance)
  - [Gallery of Examples](#gallery-of-examples)
- [Data Sources](#data-sources)
- [Dependencies](#dependencies)
- [How to Contribute](#how-to-contribute)
  - [Bug Reports & Feature Requests](#bug-reports-and-feature-requests)
  - [Developing](#developing)
- [License](#license)
- [Reaching Out](#reaching-out)
- [Support The Project :sparkling_heart:](#support-the-project-sparkling_heart)
- [Version History](#version-history)

---

## Introduction

> **cli-weather** is a command line app to get instant real-time weather data by city name or postalcode from any corner on earth right on the command line.

> Written in *python* and powered by **WeatherBIT API**, cli-weather also provides detailed weather data, air-quality data and forecasts for next 7 days with 24 hour intervals for weather and 3 days forecast with 12 hour intervals for air-quality.

> With *cli-weather app* you can retrieve current weather observations from over **45,000** live weather stations using WeatherBIT API, and highly localized weather forecasts for any point on the globe using the world's most trusted weather models such as GFS 13km, ECMWF, DWD 6.5km ICON-Europe, and NOAA 3km HRRR.!

> You can look up weather data any of the following means:
> - By entering city_name
> - By entering postal_code

--- 

## Installation


> cli-weather requires [pip](pip.pypa.io) python package manager to install.

<p align="center">
  <img src="https://raw.githubusercontent.com/vatsa287/cli-weather/master/assets/install-still-format.svg?raw=true">
</p>

+ ### Local Installation

    ```bash
    $ git clone "https://github.com/vatsa287/cli-weather"
    $ cd cli-weather/cli_weather
    $ python main.py -h
    ```

+ ### Tarball and Wheel Installation
  > Anyone one of the following is sufficient. Wheel is recommended for its faster installation.
  + Tarball
    - Download tarball file present in high-level format with tar.gz extension from Releases tab and extract to continue with [Local Installation](#local-installation)
  + Wheel
    - Download wheel file present in binary format with .whl extension from Releases tab and extract to continue with [Local Installation](#local-installation)

## Basic Usage

```bash
$ cli-weather command [-h] [-a] [-d] [-f] [-c COUNTRY] [-u {M,S,F}] city_nmae/postal_code
```

                 Detailed weather data of Bengaluru, by city-name

<p align="center">
  <img src="https://raw.githubusercontent.com/vatsa287/cli-weather/master/assets/city-detailed.svg?raw=true">
</p>

                 Basic airquality data at New York City, by postalcode

<p align="center">
  <img src="https://raw.githubusercontent.com/vatsa287/cli-weather/master/assets/postalcode-airquality.svg?raw=true">
</p>



+ ### Features at a glance
 
  + Positional and Optional arguments: v0.1.5 supports two modes of input and 5 options giving numerous cominations.
    
    |Command             | Description                   |
    |--------------------|-------------------------------|
    |city                | Get weather by city name      |
    |postalcode          | Get weather by postal code    |

    |Option          | Description                   |
    |----------------|-------------------------------|
    |-a, --airquality| Display current air quality   |
    |-f, --forecast  | Forecast on weather/airquality|
    |-c, --country   | Country of entered area       |
    |-u, --units     | Metric, Scientific, Farenheit |
    |-d, --detailed  | Display detailed weather data |
    |-h, --help      | Show this message and exit    |
  
  + Supported Units: v0.1.5 supports Metric,Scientific and Farenheit indices.
    
    |Units           | Extensions                    |
    |----------------|-------------------------------|
    |M               | Celcius, m/s, mm              |
    |S               | Kelvin, m/s, mm               |
    |F               | F, mph, in                    |

--- 

+ ## Gallery of Examples
  - This
  - Get current weather. Displays current temprature
  ```
  $ cli-weather city bengaluru
  ```

  - Get detailed current weather. Displays wide of range of weather data from snowfall to solar radiation (--detailed or -d)
  ```
  $ cli-weather city bengaluru -d
  ```

  - Get weather forecast for next 7 days with 24 hour interval (--forecast or -f)
  ```
  $ cli-weather city bengaluru -f
  ```

  - Get current air quality. Displays current Air Quality Index and its associated category (--airquality or -a)
  ```
  $ cli-weather city bengaluru -a
  ```

  - Get detailed current air quality. Displays concentration of various polloutants and health risk status (--detailed --airquality or -d -a)
  ```
  $ cli-weather city bengaluru -da
  ```

  - Get airquality forecast for next 3 days with 12 hour interval (--airquality --forecast or -a -f)
  ```
  $ cli-weather city bengaluru -af
  ```

- cli-weather supports three diffrent units namely Metric(default), Scientific and Farenheit) which can be specified using --units or -u)
```
$ cli-weather city singapore -u F
```
> Displays the temprature in Farenheit

|Units           | Extensions                    |
|----------------|-------------------------------|
|M               | Celcius, m/s, mm              |
|S               | Kelvin, m/s, mm               |
|F               | F, mph, in                    |

> Note: In order to have postalcode as a mode of of input replace city with postalcode and enter known postalcode.

--- 

## Data sources

> API : cli-weather is powered by WeatherBIT API

* [weatherbit.io](https://weatherbit.io/)

---

## Dependencies

* cli-weather requires [requests](http://docs.python-requests.org/en/latest/) >= 2.4 to run, comes bundled with the package.

---

## How to Contribute

#### Bug Reports and Feature Requests

Please use the [issue tracker](https://github.com/vatsa287/cli-weather/issues) to report any bugs or file feature requests.

#### Developing

PRs are welcome. To begin developing, do this:

1. Clone repo and create a new branch: `$ git checkout https://github.com/alichtman/stronghold -b name_for_new_branch`.

```bash
$ git clone "https://github.com/vatsa287/cli-weather"
$ git checkout -b name_for_new_branch
```
2. Make changes and test
3. Submit Pull Request with comprehensive description of changes

---

## License

![License](https://img.shields.io/badge/%20licence-%20GNU%20V3.0-yellow)

 cli-weather is made available under **[GNU License](https://img.shields.io/badge/%20licence-%20GNU%20V3.0-yellow)**

  + Copyright 2020 © <a href="https://github.com/vatsa287/cli-weather/blob/master/LICENSE" target="_blank">General Public Licence v3.0</a>.


## Reaching Out

<hr>
<p align="center">
  <i>You can connect with me here!</i>
  <p align="center">
    <a href="https://twitter.com/vasta287" alt="Twitter"><img height="32" width="32" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg"/></a>
    <a href="https://www.linkedin.com/in/vatsa287" alt="Linkedin"><img height="32" width="32" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" /></a>
    <a href="https://github.com/vatsa287" alt="GitHub"><img height="32" width="32" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" /></a>
    <a href="https://medium.com/@shreevatsan" alt="Medium"><img height="32" width="32" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/medium.svg" /></a>
  </p>
</p>
<hr>


## Support The Project :sparkling_heart:

I open-source almost everything I can, and I try to reply to everyone needing help using these projects. Obviously,
this takes time. You can use this service for free.

However, if you are using this project and happy with it or just want to encourage me to continue creating stuff, there are few ways you can do it :-

- Starring and sharing the project :rocket:
- You can donation via BuyMeACoffee. I'll probably buy a ~~coffee~~ tea. :tea:
<a
href="https://www.buymeacoffee.com/vatsa287">
<img
src="https://cdn.buymeacoffee.com/buttons/default-orange.png"
alt="Buy Me A Coffee" width="150" height="30" >
</a>

--- 

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

Thanks! :heart:
