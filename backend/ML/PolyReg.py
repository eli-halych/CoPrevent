from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd
from datetime import datetime as dt
from matplotlib import pyplot as plt

from backend.ML.utils import change_date, DATE_FORMAT

BOOL_COND_ARRAY = []

def get_trend_pred(starting_date, prediction_info, united_samples):
    """
        # TODO implement increasing/decreasing trend insight
        features are dates
        labels are values
    """

    # FIXME rn dates are a day forward
    #  SOLUTION:
    #   [done] 1. move all dates a day behind
    # TODO trend:
    #  SOLUTION:
    #  [done] 1. get a value from regression for the starting date
    #  [done] 2. get a value from regression for the ending date
    #  3. Compare values to define a trend

    features = united_samples[:, :1].astype(str)
    labels = united_samples[:, -1:]

    # move all dates a day behind
    delta = -1
    generator = (change_date(date[0], delta_days=delta) for date in features)
    new_dates = np.fromiter(generator, features.dtype)

    # selecting samples after April 2020 when the COVID-19 became global
    BOOL_COND_ARRAY = [(int(date[0:4]) >= 2020 and int(date[5:7]) >= 4)
                       for date in new_dates]
    new_dates = new_dates[BOOL_COND_ARRAY]
    new_dates = new_dates.reshape(-1, 1)

    labels = labels[BOOL_COND_ARRAY]

    # converting date to numerical source:
    generator = (dt.toordinal(dt.strptime(date[0], DATE_FORMAT)) for date in
                 new_dates)
    numerical_dates = np.fromiter(generator, features.dtype)
    numerical_dates = numerical_dates.reshape(-1, 1).astype(float)

    # change degree of polynomial features
    poly_features = PolynomialFeatures(degree=4)
    features_transformed = poly_features.fit_transform(numerical_dates)

    # model
    linreg_model = LinearRegression()
    linreg_model.fit(features_transformed, labels)

    # trend
    trend_labels = linreg_model.predict(
        poly_features.fit_transform(numerical_dates))

    # TODO remove
    viz_polymonial(numerical_dates, labels, trend_labels)

    trend = None

    return trend


def viz_polymonial(x, y, y_pred):
    plt.plot(x, y, color='red')
    plt.plot(x, y_pred, color='blue')
    plt.title('Prediction of new cases (Linear Regression)')
    plt.xlabel('Date')
    plt.ylabel('New cases')
    plt.show()
    return
