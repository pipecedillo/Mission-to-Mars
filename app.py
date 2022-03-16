from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb+srv://pipecedillo:34CQzUa7okOIxBgW@cluster0.vgexk.mongodb.net/mars_app?retryWrites=true&w=majority"
mongo = PyMongo(app)
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)
if __name__ == "__main__":
   app.run()
