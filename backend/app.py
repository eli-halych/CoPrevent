from datetime import datetime

from flask import Flask, redirect, request, abort, json, url_for, jsonify
from werkzeug.exceptions import HTTPException

from backend.ML.RNN import RNN


def create_app():
    app = Flask(__name__)

    @app.route('/survey', methods=['POST'])
    def post_survey():
        """
            Send filled out survey form data
            :return: prediction and filtered
        """

        response_data = {}

        if not request.data:
            abort(400)  # bad request

        data = request.data

        try:
            rnn = RNN(country_code=data['country_code'],
                      look_forward=data['look_froward_days'])

            # TODO make sure the available day is taken, today is dummy
            today = datetime.today()
            pred_new_cases, message = rnn.predict(today)
            pred_trend = rnn.get_trend(today)

            response_data['country_region_code'] = data['country_code']
            response_data['prediction'] = pred_new_cases
            response_data['message'] = message
            response_data['trend'] = pred_trend
            response_data['success'] = True
        except Exception as e:
            abort(422)  # unprocessable entity

        return jsonify(response_data)

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        response = e.get_response()

        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
