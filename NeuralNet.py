import pandas as pd
import csv


write_file = open('tweetDict.csv', 'a', newline='')
csv_writer = csv.writer(write_file)


def get_dict_from_csv():
    dict_df = pd.read_csv("dictionary.csv")
    return dict_df.as_matrix()


def get_dict_from_matrix(matrix):
    dictionary = []
    for row in matrix:
        dictionary.append(row[0])
    return dictionary


def synthesize_tweet_dict(dictionary, tweet):
    single_dict = []
    for word in dictionary:
        count = 0
        for tweet_word in tweet.split():
            if word == tweet_word:
                count += 1
        single_dict.append(count)
    return single_dict


def get_tweet_data():
    df = pd.read_csv("tweets_data.csv")
    return df.as_matrix()


def write_tweet(data, matrix):
    i = 1
    for row in matrix:
        print(i)
        line = row[0][2:-1]
        single_dict = synthesize_tweet_dict(data, line)
        single_dict.append(row[1])
        csv_writer.writerow(single_dict)
        i += 1


full_dict = get_dict_from_matrix(get_dict_from_csv())
write_tweet(full_dict, get_tweet_data())


