from flask import Flask
from flask_cors import CORS

from app.api import blueprint


def register_extension(flask_app: Flask):
    from app import extension
    extension.db.init_app(flask_app)
    extension.jwt.init_app(flask_app)


def create_app(*config_cls) -> Flask:
    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    register_extension(flask_app)
    CORS(flask_app)
    blueprint(flask_app)

    return flask_app
