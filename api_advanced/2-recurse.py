#!/usr/bin/python3
"""
Returns a list of titles of all hot posts in a subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively gets all hot post titles.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "python:reddit.api.project:v1.0 (by /u/student)"
    }

    params = {
        "limit": 100,
        "after": after
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json()["data"]

    posts = data["children"]

    # Add the titles from this page
    for post in posts:
        hot_list.append(post["data"]["title"])

    # If there are more pages, call the function again
    if data["after"] is not None:
        return recurse(subreddit, hot_list, data["after"])

    return hot_list
