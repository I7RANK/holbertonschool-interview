#!/usr/bin/python3
""" this module contain top_ten function """

import requests


def count_words(subreddit, word_list, hot_list=[], after=''):
    """ returns the first """
    my_header = {'user-agent': 'i7RANK'}
    par = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit,
        after
    )

    rq = requests.get(
        url,
        headers=my_header,
        allow_redirects=False,
    )

    if rq.status_code == 200:
        hot_list += rq.json().get("data", {}).get("children", [])
        affffter = rq.json().get("data", {}).get("after", None)

        if affffter:
            return count_words(
                subreddit,
                word_list,
                hot_list=hot_list,
                after=affffter
            )
        else:
            word_dict = {
                word_list[i].lower(): 0 for i in range(len(word_list))
            }

            for i in hot_list:
                title = i.get('data').get('title').lower().split()

                for k in word_list:
                    for i in title:
                        if k.lower() == i:
                            word_dict[k.lower()] += 1

            for k in sorted(word_dict.keys()):
                if word_dict[k] > 0:
                    print('{}: {}'.format(k, word_dict[k]))
