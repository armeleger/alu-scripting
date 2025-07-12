#!/usr/bin/python3
<<<<<<< HEAD
"""Module to print top 10 hot post titles"""
import requests

def top_ten(subreddit):
    """Prints the top 10 hot posts of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'CustomUserAgent/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
=======
"""Fetch and print titles of the first 10 hot posts of a subreddit."""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python:api_advanced:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
>>>>>>> adc08c674e10dbf26ccc69bd0589e0b9966b787a

    if response.status_code != 200:
        print(None)
        return

<<<<<<< HEAD
    posts = response.json().get('data', {}).get('children', [])
    for post in posts:
        print(post.get('data', {}).get('title'))
=======
    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
>>>>>>> adc08c674e10dbf26ccc69bd0589e0b9966b787a
