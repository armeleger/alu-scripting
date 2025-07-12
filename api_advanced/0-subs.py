#!/usr/bin/python3
"""Module to get number of subscribers for a subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Returns number of subscribers or 0 if subreddit is invalid"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'CustomUserAgent/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    return 0
