from flask import Flask, redirect, request, abort, json, url_for, jsonify
from werkzeug.exceptions import HTTPException


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

        try:
            # TODO call an ML model taking in requested_data
            response_data['prediction'] = 0.0  # TODO apply when ready
            response_data['message'] = ''  # TODO apply when ready
            response_data['success'] = True
            # TODO add other necessary data for the map
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
