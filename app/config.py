class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:qt217gb314@localhost/test1'
    SECRET_KEY = "qt217gb314"

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_hash = 'bcrypt'
