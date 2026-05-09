#!/usr/bin/env python3
"""
Load Twitter API credentials from environment variables.
Copy .env.example to .env and fill in your keys.
"""
import os
import tweepy

access_token        = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
API_key             = os.environ.get("TWITTER_API_KEY")
API_secret_key      = os.environ.get("TWITTER_API_SECRET_KEY")

def get_api():
    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth, wait_on_rate_limit=True)