#!/usr/bin/python3
"""Queries Reddit API to return subreddit subscriber count."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:sub.counter:v1.0 (by /u/fakeuser)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
