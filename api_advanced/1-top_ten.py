#!/usr/bin/python3
"""
Queries Reddit API and prints titles of first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts or None if invalid subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'custom-agent/1.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)
