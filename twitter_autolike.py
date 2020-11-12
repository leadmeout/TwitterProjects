from keys import keys
import tweepy
import time

# Assign variables
SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

# Create variable to authenticate yourself calling API method
# Add wait on rate limit to pause when hitting rate limit and wait for it to replenish
# Notify will print a notification to the console
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Define search term and how many tweets to pull
search = 'Python'
number_of_tweets = 500

def auto_like_tweet(search, number):
    '''
        Function for finding tweets containing search term and automatically liking it
    '''
    # Loop through a certain number of tweets using Cursor method
    for tweet in tweepy.Cursor(api.search, search).items(number):
        try:
            print("Tweet liked!")
            tweet.favorite()
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

auto_like_tweet(search, number_of_tweets)