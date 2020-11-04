import tweepy
import time

# Add API key and secret
auth = tweepy.OAuthHandler('', '')
#add access token and secret
auth.set_access_token('', '')

# create variable to authenticate yourself calling API method
# add wait on rate limit to pause when hitting rate limit and wait for it to replenish
# notify will print a notification to the console
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
            time.sleep(60)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

auto_like_tweet(search, number_of_tweets)