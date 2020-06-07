import time
import datetime as dt
from matplotlib import pyplot as plt
from keras import models
from werkzeug.exceptions import abort

# TODO save dependencies to requirements.txt
# TODO update docstrings
from backend.ML.utils import load_data, preprocess, filter_by_country, \
    separate, normalize, apply_lookback, reshape, unite_dates_samples


class RNN:
    def __init__(self, country_code, look_forward=3):
        """
        """
        if not country_code:
            abort(422)

        self.look_back = look_forward
        self.look_forward = look_forward
        self.country_code = country_code
        self.models_src = 'models_countries'
        self.model = models.load_model(
            f'{self.models_src}/{self.country_code}-RNN.h5')

    def predict(self, day):
        """
        """
        # TODO tests

        # TODO refactor: get data from database
        df = load_data()
        df = preprocess(df)
        df = filter_by_country(df, self.country_code)
        # separate cases from data
        dates, Y = separate(df)
        # normalize X
        Y = normalize(Y)
        # apply look_back and generate needed samples
        X, _ = apply_lookback(Y, look_back=1)
        # reshape to fit the model
        X = reshape(X)
        # unite with dates, consider look_back
        united_samples = unite_dates_samples(dates, X)

        last_day = day
        predicted = 0
        for step in range(self.look_forward):
            # TODO get based on the day
            sample = self.get_sample(X, last_day)

            # make predictions one step further
            predicted = self.model.predict(sample)
            # TODO append the result to X to be last-k | ... | last | predicted
            #  This will do it for predicting for multiple time stamps

            # TODO last_day += step

        message = f'In {self.look_forward} days expected number of cases ' \
            f'will be equal {predicted} '

        return predicted, message

    def get_trend(self, day):
        """
        """
        predicted, _ = self.predict(day)

        # TODO implement increasing/decreasing trend after predictions are
        #  implemented
        trend = None

        return trend

    def get_sample(self, X, day):
        """
            Takes self.lookback days behind and the corresponding new cases of
            COVID-19.

        """
        # TODO get sample based on the day and lookback days behind
        # TODO restriction - has to have lookback days behind
        return [[]]
