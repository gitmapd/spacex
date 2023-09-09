import requests
import json
from flask import jsonify
def categorize_launches(launches):
    successful = list(filter(lambda x: x["success"] and not x["upcoming"], launches))
    failed = list(filter(lambda x: not x["success"] and not x["upcoming"], launches))
    upcoming = list(filter(lambda x: x["upcoming"], launches))

    return {
        "successful": successful,
        "failed": failed,
        "upcoming": upcoming
    }

def categorize_events(launches):
    date_utc = list(x["date_utc"] for x in launches)
    name = list(x["name"] for x in launches)
    return {
            "date_utc": date_utc,
            "name": name
    }
def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v5/launches"
    response = requests.get(url)
    content = response.content
    if response.status_code == 200:
        return json.loads(content)
    else:
        return []
    
def fetch_latest_launch():
    url = "https://api.spacexdata.com/v5/launches/latest"
    response = requests.get(url)
    content = response.content
    if response.status_code == 200:
        return json.loads(content)
    else:
        return []