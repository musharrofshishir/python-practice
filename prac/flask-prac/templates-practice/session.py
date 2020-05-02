from flask import Flask, render_template, request, session
# from flask_session import Session 
app = Flask(__name__)

# app.config["SESSION_PERMANENT"] = "false"
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

notes = []

@app.route("/", methods=[ "GET", "POST" ])
def todos():
    # if session.get("notes") is None:
    #     session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        # session["notes"].append(note)
        notes.append(note)
    return render_template("todo.html", notes=notes)


if __name__ == "__main__":
    app.run( debug=True )