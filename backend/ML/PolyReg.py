from datetime import datetime as dt

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from backend.ML.utils import change_date, DATE_FORMAT

BOOL_COND_ARRAY = []


def get_trend_pred(united_samples):
    """
        # TODO implement increasing/decreasing trend insight
        features are dates
        labels are values
    """

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

    ahead = trend_labels[-1:, 0]
    behind = trend_labels[-1 - 3:-3, 0]

    if ahead > behind:
        return 'upward'
    elif ahead < behind:
        return 'downward'
    else:
        return 'not_changed'
