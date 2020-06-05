import os

from flask import Flask, render_template

template_dir = os.path.abspath('frontend/templates')
static_dir = os.path.abspath('frontend/static')

def create_app():

    app = Flask(__name__,
                template_folder=template_dir,
                static_folder=static_dir)

    @app.route('/')
    def present():
        return render_template("world.html")

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
