#!/usr/bin/python3
"""Recursive function to return hot post titles"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of hot post titles recursively"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'CustomUserAgent/0.1'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

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

