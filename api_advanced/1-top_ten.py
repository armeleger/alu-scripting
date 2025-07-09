#!/usr/bin/python3
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python:ALU-scripting:v1.0 (by /u/fakeuser)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
