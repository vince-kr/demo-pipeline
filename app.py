import business_logic
import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index() -> str:
    user_name = request.args.get("name-input") or "there"
    format_date = business_logic.long_date(datetime.date.today())
    context = {
        "name": user_name,
        "format_date": format_date,
    }
    return render_template("index.html", context=context)