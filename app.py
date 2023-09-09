from flask import Flask, render_template
from datetime import datetime
import requests
from api import api_get

app = Flask(__name__)
 
@app.template_filter("date_only")
def date_only_filter(s):
    date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted = date_object.strftime("%m-%d-%Y")
    #return date_object.date()
    return formatted
   
@app.route("/")
def index():
    return render_template('index.html',launches=launches,latest=latest)

launches = api_get.categorize_launches(api_get.fetch_spacex_launches())

latest = api_get.fetch_latest_launch()
#latest = api_get.categorize_launches_latest(api_get.fetch_latest_launch())
#print(latest)

    
if __name__ == '__main__':
    app.run(debug=True)
