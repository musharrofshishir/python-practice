import datetime
from flask import Flask, render_template 

app = Flask(__name__)

app.debug = True

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html") 

@app.route("/new")
def fun():
    now = datetime.datetime.now()
    newyear = now.month == 1 and now.day == 1
    return render_template("newyear.html", newyear=newyear)
        



if __name__== "__main__":
    app.run()