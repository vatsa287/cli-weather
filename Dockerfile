# Python as base image [slim-buster has bin/bash support and lightweight]
FROM python:3.8-slim-buster

# Set metadata
LABEL maintainer="i.mnshreevatsa@gmail.com"
LABEL version="1.0"
LABEL description="Lightweight command line app to get fast real-time weather data right on the command line ."

# Install cli-weather from PyPi
RUN pip3 install cli-weather

# Run container in script mode
CMD ["/bin/bash"]