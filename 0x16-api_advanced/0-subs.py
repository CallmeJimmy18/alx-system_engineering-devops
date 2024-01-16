#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a given subreddit """
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "linux:0x16.api:v1.0.0 (by /u/c_a_l_l_me_jimmy18)"}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")

    else:
        return 0
