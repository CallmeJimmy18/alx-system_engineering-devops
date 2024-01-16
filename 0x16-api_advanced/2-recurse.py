#!/usr/bin/python3
""" returns a list containing the titles """
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    queries the Reddit API and
    returns a list containing the
    titles of all hot articles for a given subreddit
    """

    headers = {
            "User-Agent": "linux:0x16.api:v1.0.0 (by /u/c_a_l_l_me_jimmy18)"
            }
    subr_data = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers=headers, allow_redirects=False)

    if subr_data.status_code >= 400:
        return None

    ht_list = hot_list + [article.get("data").get("title")
                          for article in subr_data.json()
                          .get("data")
                          .get("children")]

    info = subr_data.json()
    if not info.get("data").get("after"):
        return ht_list

    return recurse(subreddit, ht_list, info.get("data").get("count"),
                   info.get("data").get("after"))
