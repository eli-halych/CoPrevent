import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

COLNAMES = ['ISO_2_CODE', 'ADM0_NAME', 'date_epicrv',
            'NewCase', 'CumCase', 'NewDeath',
            'CumDeath']
NEW_COLUMN_NAMES = ['country_region_code', 'country_region', 'date',
                    'new_cases', 'cum_cases', 'new_deaths', 'cum_deaths']
DATASET_DIR = f'{os.path.dirname(__file__)}/../datasets'
FILENAME = 'who_cases_deaths.csv'
DATE_FORMAT = '%Y-%m-%d'

np.random.seed(7)
SCALER = MinMaxScaler(feature_range=(0, 1))


def load_data():
    return pd.read_csv(f'{DATASET_DIR}/{FILENAME}', usecols=COLNAMES)


def preprocess(dataframe):
    # rename column names
    mapped_columns = dict(zip(COLNAMES, NEW_COLUMN_NAMES))
    dataframe = dataframe.rename(columns=mapped_columns)

    # format date
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe['date'] = dataframe['date'].dt.strftime(DATE_FORMAT)

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


def denormalize(sample):
    return SCALER.inverse_transform(sample)


def apply_lookback(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)


def reshape(X):
    return np.reshape(X, (X.shape[0], 1, X.shape[1]))


def unite_dates_samples(dates, samples):
    """
        Unites dates to make predictions for with samples
        :return: united
    """

    return np.hstack((dates,
                      samples))


def change_date(date, delta_days=0):
    detla = timedelta(days=delta_days)
    next_date = date + detla

    return next_date


def append_sample(array, predicted, look_back, requested_day, step):
    """
    """

    # next date
    date = datetime.strptime(requested_day, DATE_FORMAT)
    next_date = change_date(date, delta_days=1)
    next_date_formatted = np.array(
        [datetime.strftime(next_date, DATE_FORMAT)]
    )

    # generate next sample
    selected = array[array[:, 0] == requested_day, 2:].reshape(look_back - 1, )
    selected = np.append(selected, predicted.reshape(1, ))
    next_sample = np.append(next_date_formatted, selected)

    # append next sample
    if len(array[array[:, 0] == next_date_formatted, :]) == 0:
        array = np.vstack((array, next_sample))
    else:
        array[array[:, 0] == next_date_formatted] = next_sample

    return array, next_date_formatted[0]
