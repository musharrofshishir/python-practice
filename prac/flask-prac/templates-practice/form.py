from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/output", methods=[ "POST" ])
def output():
    firstName = request.form.get("first_name")
    lastName = request.form.get("last_name")
    return render_template("output.html", firstName=firstName, lastName=lastName)

@app.route("/")
def form():

    return render_template("form.html")


if __name__ == "__main__":
    app.run( debug=True )