import time
import datetime as dt
from matplotlib import pyplot as plt
from keras import models
from werkzeug.exceptions import abort

# TODO save dependencies to requirements.txt
# TODO update docstrings

class RNN:
    def __init__(self, country_code, look_back=3, look_forward=3):
        """
        """
        if not country_code:
            abort(422)

        self.look_back = look_back
        self.look_forward = look_forward
        self.country = country_code
        self.models_src = 'models_countries'
        self.model = models.load_model(
            f'{self.models_src}/{self.country}-RNN.h5')

    def predict(self, day):
        """
        """
        # TODO get data by country, date with cases
        # TODO separate cases from data
        # TODO normalize cases
        # TODO apply look_back and generate needed samples
        # TODO reshape to fit the model

        sample = self.get_sample()
        predicted = self.model.predict(sample)

        return predicted

    def get_trend(self, day):
        """
        """
        predicted = self.predict(day)

        # TODO implement increasing/decreasing trend after predictions are
        #  implemented
        trend = None


        return trend

    def get_sample(self):
        """
        """
        return [[]]
