import requests
from time import sleep
from datetime import date
import os
import base64

wakapi_url = os.environ['WAKAPI_URL']

github_api, wakapi_api = 'https://api.github.com/user', wakapi_url + '/api/summary'

wakapi_key = os.environ['WAKAPI_API_KEY']
github = os.environ['GITHUB_API_KEY']

def format_seconds(seconds):
    mins = seconds // 60  # Minuten berechnen
    secs = seconds % 60   # Übrig gebliebene Sekunden berechnen

    if mins > 0:
        return f"{mins} mins {secs} secs"
    else:
        return f"{secs} secs"

while True:
    res = requests.get(wakapi_api,
    headers={
        "Authorization": f"Basic {base64.b64encode(wakapi_key.encode('ascii')).decode('ascii')}"
    },
    params={
        'interval': 'today'
    })

    if res.status_code == 200:

        res = res.json()

        time = sum(project['total'] for project in res['projects'])

        time_formatted = format_seconds(time)

        post = requests.patch(github_api, headers={
            'Accept': "application/vnd.github.v3+json",
            'Authorization': f'token {github}'
        }, json={
            'bio': f'Today ({date.today()}) coded: {time_formatted}'
        })

        if post.status_code == 200:
            print("<SUCCESS> Bio updated: " + f'Today ({date.today()}) coded: {time_formatted}')
        else:
            print("<FAIL> " + post.content)

    # Update bio every 15 minutes
    sleep(900)