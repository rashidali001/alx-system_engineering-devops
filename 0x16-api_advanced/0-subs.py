#!/usr/bin/python3
"""0-subs

Returning number of given subscribers in a 
given reddit
"""
import requests
from sys import argv


CLIENT_ID = "w-VEfwEKRlI3y8YWJyvv6Q"
SECRET_KEY = "VWYV5e2VRKYmLJ0a1uO5W5kWnmLVtA"
subreddit = argv[1]

# Get auth token from reddit
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

login_details = {
    "grant_type": "password",
    "username": "_rashidali_b",
    "password": "R@shid.254",
}

headers = {"User-Agent": "MyAPI/0.0.1"}

res = requests.post(
    "https://www.reddit.com/api/v1/access_token",
    auth=auth,
    data=login_details,
    headers=headers,
)

TOKEN = res.json()["access_token"]

headers["Authorization"] = f"bearer {TOKEN}"

# function to return subscribers
def number_of_subscribers(subreddit):
    try:
        res = requests.get(
            f"https://oauth.reddit.com/r/{subreddit}/about", headers=headers
        )
        return res.json()["data"]["subscribers"]
    except:
        return 0
