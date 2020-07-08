class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFIACTIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://newuser:password@127.0.0.1/telebot'
    SECURITY_PASSWORD_SALT = 'thisissecret'