from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Вітаю Вас!'

    @app.route('/api/v1/hello-world-20')
    def hello_world_20():
        return 'Hello World 20'

    return app
