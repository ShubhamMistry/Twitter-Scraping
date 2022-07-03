#importing the libraries
import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv

#Generating User Query
query=input("Enter the topic you want to scrape from Twitter:- ")
tweets=[]
limits=int(input("Enter the Number of Tweets you want to scrape:- "))
print("Scraping of ",query," In Progress.....")
#Main Code
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets)==limits:
        break
    else:
        tweets.append([tweet.date,tweet.user.username,tweet.content,tweet.likeCount,tweet.retweetCount])

#Creating Dataframe and storing tweets in it
df=pd.DataFrame(tweets,columns=['Date','User','Tweets','LikeCount','RetweetCount'])
print(df)

#Exporting Tweets into CSV File
df.to_csv('tweet.csv')

print("\n","!!!!!!!!!!Scraping of ",query," Done Successfully !!!!!!!!!!!")

