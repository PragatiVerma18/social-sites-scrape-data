#
#Read https://github.com/5hirish/tweet_scrapper/blob/master/USAGE.md for more details on usage.
#
#

from tweetscrape.profile_tweets import TweetScrapperProfile 
from tweetscrape.users_scrape import TweetScrapperUser

#The TweetScrapperUser class scrapes the stats of the user from Twitter. It requires one parameter, the Twitter username of the user. This method returns a JSON.
ts = TweetScrapperUser("elonmusk")
user_info = ts.get_profile_info()
for k, v in user_info.items():
    print(k,' : ', v)
#print(user_info)

#The TweetScrapperProfile class scrapes the tweets using Twitter frontend APIs with XPATH queries. It requires four parameters, the Twitter username, the number of tweets to scrape (default tweets scraped are 40), the file path to dump the data and the data export format, which can be JSON or CSV. 

tweet_scrapper = TweetScrapperProfile("elonmusk", -1, 'twitter.csv', 'csv')
#To extract as much tweets as possible set the number of tweets to -1.
tweet_count, tweet_id, tweet_time, dump_path = tweet_scrapper.get_profile_tweets()
print("Extracted {0} tweets till {1} at {2}".format(tweet_count, tweet_time, dump_path))
