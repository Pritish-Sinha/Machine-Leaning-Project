# Imports
from sklearn.model_selection import train_test_split


def unpacker_of_test_and_train_data(without_genre, genre):
    # Unpacking the training and testing data randomly
    X_train_unpacked, X_test_unpacked, y_train_unpacked, y_test_unpacked = \
        train_test_split(without_genre, genre, test_size=0.1)

    return X_train_unpacked, X_test_unpacked, y_train_unpacked, y_test_unpacked
