from flask import Flask, render_template, request, redirect, Response
from src.api import getClasses
from src.sync import generateCalendar
import os

app = Flask(__name__)


@app.route("/")
def home():
    try:
        return render_template(
            "home.html",
            classes=getClasses(),
        )
    except Exception as e:
        return e, 500


@app.route("/calendar")
def calendar():
    try:
        classId = request.args.get("class")

        if not classId:
            return redirect("/")
        ics = generateCalendar(classId)

        return Response(
            ics,
            mimetype="text/calendar",
        )
    except Exception as e:
        return e, 500


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=5000)
