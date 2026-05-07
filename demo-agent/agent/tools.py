import datetime
from zoneinfo import ZoneInfo
import random

def get_weather(query: str) -> str:
    """Simulates a web search for weather.

    Args:
        query: The location to get weather for.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


def get_current_time(query: str) -> str:
    """Simulates getting the current time for a city.

    Args:
        query: The city name.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        tz_identifier = "America/Los_Angeles"
    else:
        return f"Sorry, I don't have timezone information for query: {query}."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time for {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"


def calculator(expression: str) -> str:
    """Evaluates mathematical expressions.

    Args:
        expression: Math expression (e.g., "15 * 12").
    """
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"


def get_random_fact() -> str:
    """Provides a random interesting fact."""
    facts = [
        "Honey never spoils.",
        "A day on Venus is longer than a year on Venus.",
        "Octopuses have three hearts.",
        "The Eiffel Tower can be 15 cm taller during the summer.",
        "Bananas are berries, but strawberries aren't."
    ]
    return random.choice(facts)
