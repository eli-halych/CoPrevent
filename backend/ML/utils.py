import pandas as pd
import numpy as np

import time
import math
import datetime as dt
from matplotlib import pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

COLNAMES = ['ISO_2_CODE', 'ADM0_NAME', 'date_epicrv',
            'NewCase', 'CumCase', 'NewDeath',
            'CumDeath']
NEW_COLUMN_NAMES = ['country_region_code', 'country_region', 'date',
                    'new_cases', 'cum_cases', 'new_deaths', 'cum_deaths']
DATASET_DIR = '../datasets/'
FILENAME = 'who_cases_deaths.csv'

np.random.seed(7)
SCALER = MinMaxScaler(feature_range=(0, 1))


def load_data():
    return pd.read_csv(f'{DATASET_DIR}/{FILENAME}', usecols=COLNAMES)


def preprocess(dataframe, date_format='%Y-%m-%d'):
    # rename column names
    mapped_columns = dict(zip(COLNAMES, NEW_COLUMN_NAMES))
    dataframe = dataframe.rename(columns=mapped_columns)

    # format date
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe['date'] = dataframe['date'].dt.strftime(date_format)

    # select used columns
    dataframe = dataframe[['country_region_code', 'date', 'new_cases']]

    return dataframe


def filter_by_country(dataframe, country_code):
    filtered_df = dataframe[
        dataframe['country_region_code'] == country_code][
        ['date', 'new_cases']]
    return filtered_df


def separate(dataframe):
    X = dataframe['date'].values.reshape(-1, 1)

    dataframe['new_cases'] = dataframe['new_cases'].astype('float32')
    Y = dataframe['new_cases'].values.reshape(-1, 1)

    return X, Y


def normalize(Y):
    return SCALER.fit_transform(Y)


def apply_lookback(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)


def reshape(X):
    return np.reshape(X, (X.shape[0], 1, X.shape[1]))
