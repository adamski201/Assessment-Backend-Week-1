"""Functions for working with dates."""

from datetime import datetime

weekdays_map = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def convert_to_datetime(date: str) -> datetime:
    """Converts a string in the format DD.MM.YYYY into a Datetime object."""
    try:
        return datetime.strptime(date, "%d.%m.%Y")
    except ValueError as exc:
        raise ValueError("Unable to convert value to datetime.") from exc
    except TypeError as exc:
        raise TypeError("Unable to convert value to datetime.") from exc


def get_days_between(first: datetime, last: datetime) -> int:
    """Gets the number of days between two datetimes."""
    if not isinstance(first, datetime) or not isinstance(last, datetime):
        raise TypeError("Datetimes required.")

    return (last - first).days


def get_day_of_week_on(date: datetime) -> str:
    """Gets the named day of the week for a Datetime object."""
    if not isinstance(date, datetime):
        raise TypeError("Datetime required.")

    return weekdays_map[date.weekday()]
