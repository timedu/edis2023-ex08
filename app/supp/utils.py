
import requests # pyright: ignore
import json
from datetime import datetime
from os import environ 

from supp.config import todo, url


def get_timestamp():

    timestamp = todo['requests'].get_timestamp()

    if not timestamp:
        clock_drift_ms = int(environ.get('CLOCK_DRIFT', 0)) * 3600
        timestamp = datetime.now().timestamp() * 1000 + clock_drift_ms
    
    return timestamp


def send_request(message):

    response = todo['requests'].send_request(message)

    if isinstance(response, str):
        return response

    if not response:
        response = requests.post(url, json = message)

    if len(response.text):
        return json.dumps(response.json(), indent=4) 
