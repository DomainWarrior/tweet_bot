#!/usr/bin/env python
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("apikey", "apisecretkey")
auth.set_access_token("accesstoken",
                      "accesstokensecret")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

#this tweets manually just change the string to whatever you want
api.update_status("Yes I work as a matter of fact!")
