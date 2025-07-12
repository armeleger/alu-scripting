#!/usr/bin/python3
"""Recursive keyword counter"""
import requests

def count_words(subreddit, word_list, hot_list=[], after=None):
    """Counts keywords in hot post titles of a subreddit"""
    if not hot_list:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {'User-Agent': 'CustomUserAgent/0.1'}
        params = {'after': after}
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            return

        data = response.json().get('data', {})
        children = data.get('children', [])
        for post in children:
            hot_list.append(post.get('data', {}).get('title'))

        after = data.get('after')
        if after:
            return count_words(subreddit, word_list, hot_list, after)

    word_count = {}
    for word in word_list:
        count = sum(title.lower().split().count(word.lower()) for title in hot_list)
        if count > 0:
            word_count[word.lower()] = word_count.get(word.lower(), 0) + count

    for word in sorted(word_count.items(), key=lambda x: (-x[1], x[0])):
        print(f"{word[0]}: {word[1]}")
