#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed for a subreddit """
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints
    the titles of the first 10 hot post 
    """
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "linux:0x16.api:v1.0.0 (by /u/c_a_l_l_me_jimmy18)"}
    params = {
        "limit": 10
    }
    top = requests.get(api_url, params, headers=headers)

    if top.status_code >= 300:
        print('None')
        return


    for top_post in top.json().get("data").get("children"):
        print(top_post.get("data").get("title"))
