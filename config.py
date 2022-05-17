import os

class Config:
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTES_API_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/dbblogs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI='postgresql://ahutdjtnbfddfq:cd782ccfb813ee005fb002b65c80cbfcf358ca887ece323e9971f2e92aa4eb51@ec2-44-196-223-128.compute-1.amazonaws.com:5432/d7m7331srjqb1m'
    # DEBUG = True
    pass
    
class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}