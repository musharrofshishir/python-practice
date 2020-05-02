from flask import Flask, render_template

app = Flask(__name__)

app.debug = True

@app.route("/")
def index():
    hello = "Hello User!"
    return render_template("index.html", head=hello)

@app.route("/about")
def about():
    return render_template("about.html") 


# @app.route("/about.html")
# def about():
#     return render_template("about.html")

if __name__== "__main__":
    app.run()