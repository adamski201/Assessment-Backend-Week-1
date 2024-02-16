"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime

from flask import Flask, request, jsonify

from date_functions import convert_to_datetime, get_day_of_week_on, get_days_between

app_history = []

app = Flask(__name__)


def add_to_history(current_request):
    """Adds a route to the app history."""
    app_history.append(
        {
            "method": current_request.method,
            "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "route": current_request.endpoint,
        }
    )


@app.get("/")
def index():
    """Returns an API welcome messsage."""
    return jsonify({"message": "Welcome to the Days API."})


@app.route("/between", methods=["POST"])
def between():
    """Gets the number of days between two dates, provided in the format DD.MM.YYYY"""
    if request.headers.get("Content-Type", "") == "application/x-www-form-urlencoded":
        data = request.form
    else:
        data = request.json

    required_fields = ["first", "last"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": "Missing required data."}), 400

    try:
        first_datetime = convert_to_datetime(data["first"])
        last_datetime = convert_to_datetime(data["last"])
    except ValueError:
        return {"error": "Unable to convert value to datetime."}, 400
    except TypeError:
        return {"error": "Unable to convert value to datetime."}, 400

    days = get_days_between(first_datetime, last_datetime)

    add_to_history(request)

    return {"days": days}, 200


@app.route("/weekday", methods=["POST"])
def weekday():
    """Gets the matching weekday for a given date provided in the format DD.MM.YYYY."""
    if request.headers.get("Content-Type", "") == "application/x-www-form-urlencoded":
        data = request.form
    else:
        data = request.json

    if "date" not in data:
        return jsonify({"error": "Missing required data."}), 400

    try:
        date = convert_to_datetime(data["date"])
    except ValueError:
        return {"error": "Unable to convert value to datetime."}, 400
    except TypeError:
        return {"error": "Unable to convert value to datetime."}, 400

    add_to_history(request)

    return {"weekday": get_day_of_week_on(date)}, 200


@app.route("/history", methods=["GET"])
def history():
    """
    Get the application request history, most recent first.
    Optional parameter: Number to get (default = 5).
    """
    args = request.args.to_dict()

    page_size = 5

    if "number" in args:
        try:
            page_size = int(args["number"])

            if not 1 <= page_size <= 20:
                return {"error": "Number must be an integer between 1 and 20."}, 400

        except ValueError:
            return {"error": "Number must be an integer between 1 and 20."}, 400

    add_to_history(request)

    return app_history[-page_size:][::-1], 200


@app.route("/history", methods=["DELETE"])
def delete_history():
    """Deletes all application request history."""
    app_history.clear()
    return {"status": "History cleared"}, 200


if __name__ == "__main__":
    app.run(port=8080, debug=True)
