#!/usr/bin/python3
"""Count keywords in all hot posts of a subreddit"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, counts={}):
    if not counts:
        for word in word_list:
            counts[word.lower()] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ALX-Reddit-API/0.1"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            for keyword in counts:
                if word == keyword:
                    counts[keyword] += 1

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, hot_list, after, counts)

    sorted_counts = sorted(
        [(k, v) for k, v in counts.items() if v > 0],
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_counts:
        print(f"{word}: {count}")
