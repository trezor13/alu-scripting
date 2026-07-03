#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts of a subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the first 10 hot posts of a subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "Mozilla/5.0"
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

    posts = response.json()["data"]["children"]

    for post in posts:
        print(post["data"]["title"])
        