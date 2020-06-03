from flask import Flask, redirect


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def present():
        tmp_string = "A map is here"
        # TODO serve map: html, js, css
        return tmp_string

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
