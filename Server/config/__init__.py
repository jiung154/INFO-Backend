class Config:
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = False

    RUN_SETTING = {
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    }

    SECRET_KEY = 'dev'
    JET_SECRET_KEY = 'dev'

    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://root:tt12345678@localhost/ies'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = r'C:\Users\user\Desktop\IES\image'
