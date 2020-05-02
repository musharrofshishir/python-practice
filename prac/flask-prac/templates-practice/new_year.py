#CONDITIONS
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    currenttime = datetime.datetime.now()
    newyear = currenttime.month == 1 and currenttime.day == 1
    return render_template("newyear.html", new_year=newyear)

if __name__ == "__main__":
    app.run( debug=True )

