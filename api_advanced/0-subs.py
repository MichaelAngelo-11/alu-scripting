#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit. Returns 0 if the subreddit is invalid.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers for a subreddit, or 0 if invalid"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/fakeuser)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    except Exception:
        return 0
