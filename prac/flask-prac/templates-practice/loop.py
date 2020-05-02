from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = [ "Fish", "Chicken", "Beans", "Egg", "Meat" ]
    return render_template("looplist.html", names=names)

if __name__ == "__main__":
    app.run( debug=True )