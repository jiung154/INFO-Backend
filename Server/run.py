from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app import create_app
from app.api import blueprint
from config import Config

app = create_app(Config)

CORS(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)


if __name__ == '__main__':
    blueprint(app)

    app.run(**app.config['RUN_SETTING'])
