import environ
import requests

env = environ.Env()
environ.Env.read_env()

def wrapper(url, body):
    headers = {
        'Client-ID': env('CLIENT_ID'),
        'Authorization': env('ACCESS_TOKEN')
    }
    r = requests.post(url, headers=headers, data=body)
    return r