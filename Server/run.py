from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.update(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI=(
        'mysql+pymysql://root:tt12345678@localhost/ies')
    ,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


if __name__ == '__main__':
    '''
    from Server.app.model.account import *
    from Server.app.model.post import *

    db.drop_all()
    db.create_all()
    '''
    from Server.app.api import blueprint
    blueprint(app)

    app.run(host="0.0.0.0")
