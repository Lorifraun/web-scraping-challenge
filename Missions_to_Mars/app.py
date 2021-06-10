# import necessary libraries
Import numpy as np
from flask import Flask, render_template, jsonify, redirect

import datetime as dt
from flask pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

#mongo connection
app.config[MONGO_URI"] = "mongodb://localhost:22017/mars_db"
mongo=PyMongo(app)

# create route that renders index.html template
@app.route("/")
def index():
    
    mars=mongo.db.scrape.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scraper():

    results=scrape_mars.scrape_all()
    mongo.db.scrape.update({}. results, upsert=True)
    return redirect ("/', code=302)


if __name__ == "__main__":
    app.run(debug=True)
