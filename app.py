from flask import Flask, render_template
from datetime import datetime
import requests
from api import api_get

app = Flask(__name__)
 
@app.template_filter("date_only")
def date_only_filter(s):
    date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted = date_object.strftime("%m-%d-%Y")
    formatted2= date_object.strftime("%Y-%m-%d")
    #return date_object.date()
    return formatted

@app.template_filter("dates")
def date_only_filter(s):
    date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted2= date_object.strftime("%Y-%m-%d")
    return formatted2

@app.route("/events")
def cal():
    return render_template('calendar.html',events=events) 

@app.route("/")
def index():
    return render_template('index.html',launches=launches,latest=latest)


latest = api_get.fetch_latest_launch()

launches = api_get.categorize_launches(api_get.fetch_spacex_launches())

events = api_get.categorize_events(api_get.fetch_spacex_launches())

    
if __name__ == '__main__':
    app.run(debug=True)
