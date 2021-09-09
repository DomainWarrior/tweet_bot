import json
import textwrap
from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.contrib.sites import requests
from wallpaper import Wallpaper
from main import api


def get_quote():
    URL = "https://api.quotable.io/random"
    try:
        response = requests.get(URL)
    except:
        print("Error while calling API...")

    res = json.loads(response.text)
    return res['content'] + "-" + res['author']


def respondToTweet(last_id):
    mentions = api.mentions_timeline(last_id, tweet_mode='extended')
    if len(mentions) == 0:
        return

    for mention in reversed(mentions):
        new_id = mention.id

        if '#fod' in mention.full_text.lower():
            try:
                tweet = get_quote()
                Wallpaper.get_wallpaper(tweet)

                media = api.media_upload("created_image.png")

                api.create_favorite(mention.id)
                api.update_status('@' + mention.user.screen_name + " Here's your fact",
                                  mention.id, media_ids=[media.media_id])
            except:
                print("Already replied to {}".format(mention.id))
