# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tweepy


#how to make sure your credientals work uncomment the following lines by removing #

# Authenticate to Twitter
#auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
#auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

#api = tweepy.API(auth, wait_on_rate_limit=True,
             #    wait_on_rate_limit_notify=True)
#try:
  #  api.verify_credentials()
   # print("Authentication OK")
#except:
  #  print("Error during authentication")

  #check someones posts
#timeline = api.home_timeline()
#for tweet in timeline:
 #   print(f"{tweet.user.name} said {tweet.text}")

  #update your status one time
#    api.update_status("Test tweet from Tweepy Python")

#change your profile description with this code:
#api.update_profile(description="I like facts, I am now a fact bot! I will update at hour intervals with facts!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
