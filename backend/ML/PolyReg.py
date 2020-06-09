from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd
from datetime import datetime as dt

from backend.ML.utils import change_date, DATE_FORMAT


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
    #  1. get a value from regression for the starting date
    #  2. get a value from regression for the ending date
    #  3. Compare values to define a trend

    features = united_samples[:, :1].astype(str)
    labels = united_samples[:, -1:]

    # move all dates a day behind
    delta = -1
    generator = (change_date(date[0], delta_days=delta) for date in features)
    new_dates = np.fromiter(generator, features.dtype)
    new_dates = new_dates.reshape(-1, 1)

    # converting date to numerical source:
    generator = (dt.toordinal(dt.strptime(date[0], DATE_FORMAT)) for date in features)
    numerical_dates = np.fromiter(generator, features.dtype)
    numerical_dates = numerical_dates.reshape(-1, 1).astype(float)

    poly_features = PolynomialFeatures(degree=4)
    features_transformed = poly_features.fit_transform(numerical_dates)

    linreg_model = LinearRegression()
    linreg_model.fit(features_transformed, labels)


    trend = None

    return trend