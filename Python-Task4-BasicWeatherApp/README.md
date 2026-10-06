# Task 4 — Basic Weather App

A Beginner-tier Python command-line app that looks up current weather for a city name or postal code and displays the temperature, humidity, condition, and wind speed.

## Requirements

- Python 3.10 or newer
- Internet connection
- requests package
- No API key is required for the Open-Meteo geocoding and forecast endpoints used here.

## Setup and run

From this folder, run:

    python -m pip install -r requirements.txt
    python main.py

On Windows, use py in place of python if needed. Enter a city name or postal code when prompted. The app prints both Celsius and Fahrenheit, relative humidity, a readable weather condition, and wind speed in km/h.

## Error handling

- Empty input is rejected before making a request.
- A city or postal code with no match gets a clear message.
- Network timeouts, connection failures, HTTP errors, service errors, invalid access/API-key responses, and unreadable JSON are handled without a traceback.

Open-Meteo does not require an API key for this use, so there is no user key to register or expose. Its geocoding search accepts either a location name or postal code. Weather condition codes are mapped in main.py using the WMO interpretation table in the API docs.

## Data and privacy

The entered city name or postal code is sent to Open-Meteo's geocoding service. The returned coordinates are then sent to its forecast service. The app does not save the query or weather data locally.

## Evidence

Save a genuine run transcript or screenshot in evidence/ after running the app with an example city or postal code. Weather values change over time, so do not present a written example as a live result.

## Sources

- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api)
- [Open-Meteo Weather Forecast API](https://open-meteo.com/en/docs)
