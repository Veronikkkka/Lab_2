"""Connect front and back ends"""
from flask import Flask, redirect, render_template, request, url_for
import json
import twitter2


app = Flask(__name__)
@app.route("/map")
def index():
    """
    Open html page with map
    """
    return render_template("Map.html")

@app.route("/", methods = ["POST", "GET"])
def search():
    """
    If request was send, give
    nick of user to twitter2, else
    open start page
    """
    if request.method == "POST":
        nick = request.form["nick"]
        if twitter2.request_(nick):
            # if process_json.result(nick):
            return redirect(url_for("index"))
    else:
        return render_template("index.html")
    
app.run(debug=False)
