#!/usr/bin/python3
"""Module to print top 10 hot post titles"""
import requests

def top_ten(subreddit):
    """Prints the top 10 hot posts of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'CustomUserAgent/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get('data', {}).get('children', [])
    for post in posts:
        print(post.get('data', {}).get('title'))
