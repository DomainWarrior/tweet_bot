import tweepy
from time import sleep

import credentials
from credentials import *

#calling credentials and importing the keys
auth = tweepy.OAuthHandler(credentials.API_key, credentials.API_secret_key)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

#this is where the file is being opened read and closed for the tweets being posted
my_file = open('fact.txt', 'r', encoding="utf8")
file_lines = my_file.readlines()
my_file.close()


# Tweet a line every 15 minutes change timer to make it longer or shorter or create another command and change it to make one for the hour!
def tweet():
    for line in file_lines:
        try:
            print(line)
            if line != '\n':
                api.update_status(line)
                sleep(900)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)


tweet()
