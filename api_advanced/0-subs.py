#!/usr/bin/python3
"""Return the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Python:api_advanced:v1.0 (by /u/yourusername)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
