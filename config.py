class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test1.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1234qweasdz222222222222222222222222222222222xc'
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
