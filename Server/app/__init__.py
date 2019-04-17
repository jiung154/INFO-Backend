from flask import Flask


def create_app(*config_cls) -> Flask:
    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    return flask_app
