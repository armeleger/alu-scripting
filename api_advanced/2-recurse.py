#!/usr/bin/python3
"""Recursively return list of all hot article titles for a subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python:api_advanced:v1.0 (by /u/yourusername)"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    if data.get("after"):
        return recurse(subreddit, hot_list, data.get("after"))
    return hot_list
