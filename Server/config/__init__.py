from datetime import timedelta


class Config:
    HOST = ''
    PORT = 5000
    DEBUG = False

    RUN_SETTING = {
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    }

    SECRET_KEY = 'dev'
    JET_SECRET_KEY = 'dev'

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(7)

    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://root:tt12345678@localhost/ies'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = r'C:\Users\user\Desktop\IES\image'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


class TestConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI  = (
        'mysql+pymysql://root:tt12345678@localhost/ies_test'
    )
