import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    POSTS_PER_PAGE = 5
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['yourname@yourmail.com']
    GLOBAL_EMAIL = ['no-reply@youremail.com']
    BASE_API_URL = "http://dblp.org/search/"
    PUBLICATIONS_API_URL = BASE_API_URL + "publ/api"
    FORMAT = "json"
    H_RESULTS = 20
    BOKMARKS_PER_PAGE = 10