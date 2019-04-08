from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__)
app.config.update(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI=(
        'mysql+pymysql://<id>:<pw>@localhost/<database>')
    ,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    JWT_SECRET_KEY='dev'
)

CORS(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)


if __name__ == '__main__':

    from app.model.account import *
    from app.model.post import *

    db.drop_all()
    db.create_all()

    from Server.app.api import blueprint
    blueprint(app)

    app.run(host="0.0.0.0")
