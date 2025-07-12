#!/usr/bin/python3
<<<<<<< HEAD
"""Recursive function to return hot post titles"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of hot post titles recursively"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'CustomUserAgent/0.1'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
=======
"""Recursively return list of all hot article titles for a subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python:api_advanced:v1.0 (by /u/yourusername)"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
>>>>>>> adc08c674e10dbf26ccc69bd0589e0b9966b787a

    if response.status_code != 200:
        return None

<<<<<<< HEAD
    data = response.json().get('data', {})
    children = data.get('children', [])

    if not children:
        return hot_list

    for post in children:
        hot_list.append(post.get('data', {}).get('title'))

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list

=======
    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    if data.get("after"):
        return recurse(subreddit, hot_list, data.get("after"))
    return hot_list
>>>>>>> adc08c674e10dbf26ccc69bd0589e0b9966b787a
