from flask import Flask, render_template
from markupsafe import escape



home = Flask(__name__)

@home.route("/")
def index():
    return render_template("index.html")



home.run(host='0.0.0.0',port=81,debug=True)