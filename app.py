from flask import Flask, render_template
from src.api import getClasses
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


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=5000)
