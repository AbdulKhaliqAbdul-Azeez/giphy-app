# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os
 
# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

# add route for your gif route
@app.route("/yourgif", methods = ["GET", "POST"])
def yourgif():
    user_response = request.form["gifchoice"]
    gif_link = getImageUrlFrom(user_response)
    gif_link2 = getImageUrlFrom(user_response)
    # get the gif from giphy and puts the link on the webpage
    return render_template("yourgif.html", gif_link = gif_link, gif_link2 = gif_link2, time = datetime.now() )
    # datetime,now() to trick our browser into updating the CSS