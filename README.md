﻿[![BuiltWithPython](https://img.shields.io/badge/Built%20With%20-Python-orange?style=for-the-badge&logo=python&logoColor=green)](https://img.shields.io/badge/Built%20With%20-Python-orange?style=for-the-badge&logo=python?logoColor=green)
# cli-weather  [![Downloads](https://pepy.tech/badge/cli-weather)](https://pepy.tech/project/cli-weather)

<p align="center">
  <img src="https://raw.githubusercontent.com/vatsa287/cli-weather/master/assets/showhelp2.svg?raw=true">
</p>

---

![PyPI - Status](https://img.shields.io/pypi/status/cli-weather?color=green&style=plastic&logo=pypi&logoColor=white)  ![PyPI - Wheel](https://img.shields.io/pypi/wheel/cli-weather?color=green&style=plastic&logo=pypi&logoColor=white)  ![GitHub issues](https://img.shields.io/github/issues/vatsa287/cli-weather?color=green&style=plastic&logo=github&logoColor=white)  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/vatsa287/cli-weather?color=green&style=plastic&logo=github&logoColor=white)  ![Docker Pulls](https://img.shields.io/docker/pulls/vatsa287/cli-weather?color=green&logoColor=white&style=plastic&logo=docker)

---

## Table of Contents

- [cli-weather  ![Downloads](https://pepy.tech/project/cli-weather)](#cli-weather--)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Basic Usage](#basic-usage)
  - [Data sources](#data-sources)
  - [Dependencies](#dependencies)
  - [Version History](#version-history)
  - [How to Contribute](#how-to-contribute)
      - [Bug Reports and Feature Requests](#bug-reports-and-feature-requests)
      - [Developing](#developing)
  - [License](#license)
  - [Reaching Out](#reaching-out)
  - [Support The Project :sparkling_heart:](#support-the-project-sparkling_heart)

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

+ ### Docker Container
  > Containerized version of cli-weather is present in `DockerHub` at https://hub.docker.com/r/vatsa287/cli-weather. Steps to use cli-weather in a container
  + Pull Image
    - Latest containerized version tag is 1.0
      ```bash
      $ docker pull vatsa287/cli-weather:1.0
      ```
  + List Image
    - Check to confirm right tag
      ```bash
      $ docker image ls
      ```

  + Run Container
    - Run the container in interactive mode, also expose the terminal for input and --rm=true to save memory usage. Port mapping is optional.

      ```bash
      $ docker run -it --rm=true vatsa287/cli-weather:1.0
      ```
      Can continue further with [usage](#basic-usage).

---

## Basic Usage

> Note: Airquality information will not be available from version v1.0.0 since source API is now premium.

```bash
$ cli-weather command [-h] [-a] [-d] [-f] [-c COUNTRY] [-u {M,S,I}] city_nmae/postal_code
```

> Example : `Detailed weather data` and `Brief airquality data` with input mode as city_name and postal_code respectively.

<p align="center">
  <img src="https://raw.githubusercontent.com/vatsa287/cli-weather/master/assets/city-detailed.svg?raw=true">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/vatsa287/cli-weather/master/assets/postalcode-airquality.svg?raw=true">
</p>



+ ### Features at a glance

  + Positional and Optional arguments: v0.1.9 supports two modes of input and 5 options giving numerous cominations.

    |Command             | Description                   |
    |--------------------|-------------------------------|
    |city                | Get weather by city name      |
    |postalcode          | Get weather by postal code    |

    |Option          | Description                   |
    |----------------|-------------------------------|
    |-a, --airquality| Display current air quality   |
    |-f, --forecast  | Forecast on weather/airquality|
    |-c, --country   | Country of entered area       |
    |-u, --units     | Metric, Scientific, Imperial  |
    |-d, --detailed  | Display detailed weather data |
    |-h, --help      | Show this message and exit    |

  + Supported Units: v0.1.5 supports Metric,Scientific and Farenheit indices.

    |Units           | Extensions                    |
    |----------------|-------------------------------|
    |M               | Celcius, m/s, mm              |
    |S               | Kelvin, m/s, mm               |
    |I               | F, mph, in                    |

---

+ ## Gallery of Examples

  Check [manual](https://github.com/vatsa287/cli-weather/blob/master/docs/manual.md) for comprehensive demo of all possible options with examples.

---

## Data sources

> API : cli-weather is powered by WeatherBIT API

* [weatherbit.io](https://weatherbit.io/)

---

## Dependencies

* cli-weather requires [requests](http://docs.python-requests.org/en/latest/) >= 2.4 to run, comes bundled with the package.

---

## Version History

Latest : ![PyPI](https://img.shields.io/pypi/v/cli-weather?color=blue&label=PyPI&logo=python&logoColor=yellow&style=plastic)

Description of all versions is present [here](https://github.com/vatsa287/cli-weather/blob/master/docs/version_history.md).

---

## How to Contribute

#### Bug Reports and Feature Requests

Please use the [issue tracker](https://github.com/vatsa287/cli-weather/issues) to report any bugs or file feature requests.

#### Developing

PRs are welcome. To begin developing, do this:

1. Clone repo and create a new branch:

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

Thanks! :heart:
