from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def get_trend_pred(starting_date, prediction_info, united_samples):
    """
        # TODO implement increasing/decreasing trend insight
        features are dates
        labels are values
    """

    # FIXME rn dates are a day forward
    #  SOLUTION:
    #  1. keep the last date
    #  2. move all dates a day behind
    # TODO trend:
    #  SOLUTION:
    #  1. get a value from regression for the starting date
    #  2. get a value from regression for the ending date
    #  3. Compare values to define a trend

    features = united_samples[:, :1]
    labels = united_samples[:, -1:]

    # poly_features = PolynomialFeatures()
    # features_transformed = poly_features.fit_transform(features.reshape(-1, 1))
    #
    # linreg_model = LinearRegression()
    # linreg_model.fit(features_transformed, labels.reshape(-1, 1))
    # y_pred = linreg_model.predict(poly_features.fit_transform(features.reshape(-1, 1)))
    # # viz_polymonial(X_train_sort, y_train_sort, y_pred)

    trend = None

    return trend