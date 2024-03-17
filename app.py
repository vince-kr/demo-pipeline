import nldb
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    format_date = nldb.beauty_date()
    return render_template("index.html", format_date=format_date)