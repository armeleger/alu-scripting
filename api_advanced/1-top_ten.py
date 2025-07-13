#!/usr/bin/python3
"""
Prints titles of the top 10 hot posts from a given subreddit using Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the first 10 hot post titles.
    Prints None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'custom-user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
