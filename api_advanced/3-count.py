#!/usr/bin/python3
"""
Counts keyword occurrences in hot article titles of a subreddit using Reddit API.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively counts keywords in the hot titles of a subreddit.
    Prints the sorted results. Skips subreddit if invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0) + title.count(word_lower)

    after = data.get("after")
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        filtered = {k: v for k, v in word_count.items() if v > 0}
        for word in sorted(filtered.items(), key=lambda x: (-x[1], x[0])):
            print(f"{word[0]}: {word[1]}")
