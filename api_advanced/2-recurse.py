#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:ALU-scripting:v1.0 (by /u/fakeuser)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    posts = data['children']
    for post in posts:
        hot_list.append(post['data']['title'])

    if data['after']:
        return recurse(subreddit, hot_list, data['after'])
    return hot_list
