"""Tests for the date functions file."""

from datetime import datetime

import pytest

from date_functions import convert_to_datetime, get_days_between, get_day_of_week_on


@pytest.mark.parametrize("inp, out", (("12.01.1999", (12, 1, 1999)),
                                      ("03.04.2004", (3, 4, 2004)),
                                      ("28.02.0100", (28, 2, 100))))
def test_convert_to_datetime(inp, out):
    """Checks that the function handles valid input."""

    result = convert_to_datetime(inp)
    assert isinstance(result, datetime)
    assert result.day == out[0]
    assert result.month == out[1]
    assert result.year == out[2]


@pytest.mark.parametrize("inp", (("31.02.2013", "red.blue.green", "02/02/2002")))
def test_convert_to_datetime_rejects_bad_input(inp):
    """Checks that the function handles invalid input."""

    with pytest.raises(ValueError) as err:
        assert convert_to_datetime(inp)

    assert err.value.args[0] == "Unable to convert value to datetime."


@pytest.mark.parametrize("first, last, out", ((datetime(2023, 1, 1), datetime(2024, 1, 1), 365),
                                              (datetime(2023, 1, 1), datetime(2023, 1, 2), 1),
                                              (datetime(2023, 1, 1), datetime(2023, 2, 1), 31),
                                              (datetime(2023, 2, 1), datetime(2023, 3, 1), 28),
                                              (datetime(2024, 2, 1), datetime(2024, 3, 1), 29)))
def test_get_days_between(first, last, out):
    """Checks that the function handles valid input."""

    result = get_days_between(first, last)
    assert isinstance(result, int)
    assert result == out


@pytest.mark.parametrize("first, last", ((datetime(2023, 1, 1), None),
                                         ("", datetime(2023, 1, 2)),
                                         ("(datetime(2023, 1, 1)", datetime(2023, 2, 1)),
                                         (37, datetime(2023, 3, 1)),
                                         (datetime(2024, 2, 1), datetime)))
def test_get_days_between_invalid_input(first, last):
    """Checks that the function handles valid input."""

    with pytest.raises(TypeError) as err:
        assert get_days_between(first, last)

    assert err.value.args[0] == "Datetimes required."


@pytest.mark.parametrize("inp, out", ((datetime(2023, 10, 10), "Tuesday"),
                                      (datetime(2023, 10, 11), "Wednesday"),
                                      (datetime(2023, 10, 12), "Thursday"),
                                      (datetime(2023, 10, 14), "Saturday"),))
def test_get_day_of_week_on(inp, out):
    """Checks that the function handles valid input."""

    result = get_day_of_week_on(inp)

    assert isinstance(result, str)
    assert result.title() == result
    assert result == out


@pytest.mark.parametrize("inp", (None,
                                 "a real date",
                                 33,
                                 False,
                                 "13/3/2012"))
def test_get_day_of_week_on_invalid(inp):
    """Checks that the function handles invalid input."""

    with pytest.raises(TypeError) as err:
        get_day_of_week_on(inp)

    assert err.value.args[0] == "Datetime required."
