import environ
import requests
import time

env = environ.Env()
environ.Env.read_env()

# Wrapper used to access IGDB API endpoints for various functions and return JSON
def wrapper(url, body):
    headers = {
        'Client-ID': env('CLIENT_ID'),
        'Authorization': env('ACCESS_TOKEN')
    }
    r = requests.post(url, headers=headers, data=body)
    return r.json()

# Function used to get recently released games or soon to be released games from IGDB
def release(body):
    url = 'https://api.igdb.com/v4/release_dates'
    current_time = time.time()
    curr_time = str(current_time)
    body2 = body[:87] + curr_time[:-8] + body[87:]
    r = wrapper(url, body2)
    return r