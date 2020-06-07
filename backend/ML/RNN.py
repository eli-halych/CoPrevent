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

    def load_model(self):
        return models.load_model(f'{self.models_src}/{self.country}-RNN.h5')

    def predict(self):
        pass

    def get_trend(self):
        pass


