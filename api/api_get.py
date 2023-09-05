import requests

def categorize_launches(launches):
    successful = list(filter(lambda x: x["success"] and not x["upcoming"], launches))
    failed = list(filter(lambda x: not x["success"] and not x["upcoming"], launches))
    upcoming = list(filter(lambda x: x["upcoming"], launches))

    return {
        "successful": successful,
        "failed": failed,
        "upcoming": upcoming
    }

def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []