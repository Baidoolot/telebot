class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFIACTIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://newuser:password@localhost/telebot'
    SECURITY_PASSWORD_SALT = 'thisissecret'