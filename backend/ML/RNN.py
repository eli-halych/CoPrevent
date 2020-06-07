import time
import datetime as dt
from matplotlib import pyplot as plt
from keras import models
from werkzeug.exceptions import abort

from .utils import look_back_dataset, \
                  normalize, \
                  split, \
                  reshape, \
                  transform, \
                  transform_predict, \
                  rmse, \
                  plot

# TODO save dependencies to requirements.txt


class RNN:
    def __init__(self, country_code, look_back=3):
        if not country_code:
            abort(422)

        self.look_back = look_back
        self.country = country_code
        self.models_src = 'models_countries'
        self.model = models.load_model(f'{self.models_src}/{self.country}-RNN.h5')

    def predict(self, day):
        """
            Takes current or last available day
            :param day:
            :return: prediction of the new number of cases
        """
        sample = self.get_sample(day)
        predict = self.model.predict(sample)

    def get_trend(self, day):
        """
        Return a insight based on user's input which is a country and a day
        :param day:
        :return: prediction trend
        """
        predicted = self.predict(day)
        response = None
        return response

    def get_sample(self, day):
        pass


