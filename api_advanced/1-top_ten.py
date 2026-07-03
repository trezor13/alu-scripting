#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts of a subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "python:reddit.api.project:v1.0 (by /u/student)"
    }

    params = {
        "limit": 10
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print("None")
        return

    data = response.json()["data"]["children"]

    for post in data:
        print(post["data"]["title"])
        