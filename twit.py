

import tweepy
import json
#from pymongo import MongoClient

#client = MongoClient("mongodb://localhost:27017/")
#db = client.example


class StreamListener(tweepy.StreamListener): 
    def on_error(self, status_code):
        print status_code
        return

    def on_data(self, data):
        print data
        #datajson = json.loads(data)
        #db.tweets.insert(datajson)
        #print datajson

A_TOKEN = "2596736233-IzFD20PyKkprVnsa1G5eQ2dcoxrHpXivj6jfa6z"
A_SECRET = "C1pB7GdE8xTfS6WgJIKcipMdGu2gsseKOzxKW4skcXt4g"
C_KEY = "3Ci8ZN0XiDLYF3pAB0QnQj6jc"
C_SECRET = "wUNAYHHUFXxFVhtfqhmV1HRuOqmcu4CaiOr6sWiILNM6tDN2EF"

"""
C_KEY = "jTP8xxxxxxxxxxxxxxxxxxbLzcJY"
C_SECRET = "WYy0cZxxxxxxxxxxxxxxxxxxxx9ywCKwZT2wloHp9zSS"
A_TOKEN = "22615548xxxxxxxxxxxxxxxxxxxxxx7QLKVzWwGP7Wsll"
A_SECRET = "KsJ3muxxxxxxxxxxxxxxxxYLbgmbI9GxRzlQ9"
"""

auth1 = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth1.set_access_token(A_TOKEN, A_SECRET)

l = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
stream = tweepy.Stream(auth=auth1, listener=l)

stream.filter(track=["car"])