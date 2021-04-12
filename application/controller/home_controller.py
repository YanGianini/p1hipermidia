from application import app
from flask import render_template, redirect, request, url_for


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video")
def video():
    render_template("videos.html")
