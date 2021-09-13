from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:

    def __init__(self, username, password):

        self.username = 'youremailhere'
        self.password = 'yourpasswordhere'
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(5)

        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')

        email.clear()
        password.clear()

        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(5)

        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(5)
            tweets = bot.find_element_by_xpath('//article[@data-testid="tweet"]')
            # the following line is currently broken.
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]

            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(5)
                except Exception as ex:
                    time.sleep(60)

ed = TwitterBot('your email here','your password here')
ed.login()
# the hashtag you want to get followers from
ed.like_tweet('webdevlopment')
