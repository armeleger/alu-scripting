#!/usr/bin/python3
"""
Recursively retrieves all hot article titles for a subreddit using Reddit API.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of all hot article titles for a given subreddit.
    Returns None if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    for child in children:
        hot_list.append(child.get("data", {}).get("title"))

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
