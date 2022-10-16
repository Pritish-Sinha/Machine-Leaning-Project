# Imports
from pandas import read_csv


def reader_and_divider():
    # music_data is a data frame with the values of the given file
    music_data = read_csv('music.csv')

    # X is the data frame without the column genre
    X_return = music_data.drop(columns=['genre'])

    # y is the data frame with only genre as te
    y_return = music_data['genre']

    return X_return, y_return
