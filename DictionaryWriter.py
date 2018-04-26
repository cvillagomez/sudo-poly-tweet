import pandas as pd
import csv


dictionary = open('dictionary.csv', 'a', newline='')
csvwriter = csv.writer(dictionary)


def get_data():
    df = pd.read_csv("tweets_data.csv")
    return df.as_matrix()


def create_dataset(matrix):
    for row in matrix:
        line = row[0][2:-1]
        for word in line.split():
            csvwriter.writerow([word])


create_dataset(get_data())


