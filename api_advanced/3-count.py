#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, word_count={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:ALU-scripting:v1.0 (by /u/fakeuser)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()['data']
    posts = data['children']

    for post in posts:
        title_words = post['data']['title'].lower().split()
        for word in word_list:
            count = title_words.count(word.lower())
            if count > 0:
                word_lower = word.lower()
                if word_lower in word_count:
                    word_count[word_lower] += count
                else:
                    word_count[word_lower] = count

    if data['after']:
        return count_words(subreddit, word_list, hot_list, data['after'], word_count)

    if word_count:
        sorted_counts = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")