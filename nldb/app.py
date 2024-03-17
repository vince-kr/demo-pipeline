import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    format_date = datetime.date.today().strftime("%A %d %B %Y")
    return render_template("index.html", format_date=format_date)