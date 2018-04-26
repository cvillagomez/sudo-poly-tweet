import tweepy
import wikipedia
import csv
import sys
import pandas as pd

def get_data():
    df = pd.read_csv("twitter_handles.csv")
    return df.as_matrix()

handles = []

def fill_handles_array(matrix):
    for row in matrix:
        handles.append(row)


consumer_key = 'Os3G3T2AHSSM8MfQfAMLd8VQq'
consumer_secret = 'LjQkktOoMwpEQrVG7mqIGpF72KJHb8EgnXQhrbDWtoGhJQwyFG'

access_token = '979796826793455616-ea63A0llLRQ6sPYD10wR2DU9Onu4P6k'
access_token_secret = '18q4iKFK764Q4NOdVZyVEAaiN29Wk0yeHWVumfaD6Zzme'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

dataset = open('tweets_data.csv', 'a', newline='')
csvwriter = csv.writer(dataset)

api = tweepy.API(auth)

fill_handles_array(get_data())

j = 1

for handle in handles:
    public_tweets = api.user_timeline(screen_name=handle[0], count=200, include_rts=False, tweet_mode="extended")
    print(j)
    j += 1
    i = 1

    politicianStatus = '-1'
    isDemocrat = False
    isRepublican = False
    isPolitician = False

    for tweet in public_tweets:
        if i == 1:
            if tweet.user.verified:
                pageCategories = wikipedia.page(tweet.user.name).categories
                for category in pageCategories:
                    if category.find("politician") != -1:
                        isPolitician = True
                    if category.find("Democrats") != -1:
                        isDemocrat = True
                    if category.find("Republicans") != -1:
                        isRepublican = True
                if isPolitician:
                    if isDemocrat and not isRepublican:
                        politicianStatus = '1'
                    elif isRepublican and not isDemocrat:
                        politicianStatus = '2'
                    else:
                        politicianStatus = '0'
        if isPolitician:
            if not tweet.truncated:
                csvwriter.writerow([tweet.full_text.encode(sys.stdout.encoding, errors='replace'), politicianStatus])
        i += 1
