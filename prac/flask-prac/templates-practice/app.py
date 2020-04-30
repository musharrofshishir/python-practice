from flask import Flask, render_template

app = Flask(__name__)

app.debug = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<string:name>")
def home(name):
    if name == "about.html":
        return render_template("about.html")
    elif name == "index.html":
        return render_template("index.html")
    else:
        return render_template("index.html")
# @app.route("/about.html")
# def about():
#     return render_template("about.html")

if __name__== "__main__":
    app.run()