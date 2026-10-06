"""Fetch and display current weather for a city name or postal code."""

import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT_SECONDS = 10

WEATHER_DESCRIPTIONS = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    97: "Heavy thunderstorm",
    99: "Thunderstorm with heavy hail",
}


class WeatherLookupError(Exception):
    """A user-friendly weather lookup failure."""


class LocationNotFound(WeatherLookupError):
    """The location service returned no matching city or postal code."""


def parse_json_response(response: requests.Response, service_name: str) -> dict:
    """Check an HTTP response and return a JSON object or a clear error."""
    if response.status_code in {401, 403}:
        raise WeatherLookupError(
            f"{service_name} rejected the request (access or API-key error)."
        )
    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        raise WeatherLookupError(
            f"{service_name} returned an HTTP {response.status_code} error."
        ) from error

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError as error:
        raise WeatherLookupError(f"{service_name} returned unreadable data.") from error

    if not isinstance(data, dict):
        raise WeatherLookupError(f"{service_name} returned an unexpected response.")
    if data.get("error"):
        raise WeatherLookupError(data.get("reason", f"{service_name} reported an error."))
    return data


def find_location(query: str) -> dict:
    """Find the first geocoding result for a city name or postal code."""
    try:
        response = requests.get(
            GEOCODING_URL,
            params={"name": query, "count": 1, "language": "en", "format": "json"},
            timeout=TIMEOUT_SECONDS,
        )
    except requests.Timeout as error:
        raise WeatherLookupError("The location search timed out. Please try again.") from error
    except requests.RequestException as error:
        raise WeatherLookupError("Could not reach the location service. Check your connection.") from error

    data = parse_json_response(response, "The location service")
    results = data.get("results") or []
    if not results:
        raise LocationNotFound(f"No city or postal code matched '{query}'.")
    return results[0]


def fetch_current_weather(location: dict) -> tuple[dict, dict]:
    """Fetch current conditions for a geocoded location."""
    try:
        response = requests.get(
            WEATHER_URL,
            params={
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
                "temperature_unit": "celsius",
                "wind_speed_unit": "kmh",
                "timezone": "auto",
            },
            timeout=TIMEOUT_SECONDS,
        )
    except requests.Timeout as error:
        raise WeatherLookupError("The weather request timed out. Please try again.") from error
    except requests.RequestException as error:
        raise WeatherLookupError("Could not reach the weather service. Check your connection.") from error

    data = parse_json_response(response, "The weather service")
    current = data.get("current")
    if not isinstance(current, dict):
        raise WeatherLookupError("The weather service did not return current conditions.")
    return current, data.get("current_units", {})


def display_weather(location: dict, current: dict, units: dict) -> None:
    """Display the Task List's required current-weather fields."""
    name_parts = [location.get("name", "Selected location")]
    for part in (location.get("admin1"), location.get("country")):
        if part and part not in name_parts:
            name_parts.append(part)

    temperature_c = float(current["temperature_2m"])
    temperature_f = temperature_c * 9 / 5 + 32
    humidity = current["relative_humidity_2m"]
    wind_speed = current["wind_speed_10m"]
    weather_code = int(current["weather_code"])
    description = WEATHER_DESCRIPTIONS.get(weather_code, f"Unknown weather code ({weather_code})")
    wind_unit = units.get("wind_speed_10m", "km/h")

    print(f"\nCurrent weather for {', '.join(name_parts)}")
    print(f"Temperature: {temperature_c:.1f} °C / {temperature_f:.1f} °F")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description}")
    print(f"Wind speed: {wind_speed} {wind_unit}")


def main() -> None:
    print("Basic Weather App")
    query = input("Enter a city name or postal code: ").strip()
    if not query:
        print("Please enter a city name or postal code.")
        return

    try:
        location = find_location(query)
        current, units = fetch_current_weather(location)
        display_weather(location, current, units)
    except WeatherLookupError as error:
        print(f"Weather lookup failed: {error}")


if __name__ == "__main__":
    main()
