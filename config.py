# to set the debug mode to true=
# use terminal commmand
# FLASK_ENV = development
# flask run


#  SAMPLE CONTENT OF THE CONFIG FILE
# The config.py contains settings and configuration for your Flask application.
# import os

# app_dir = os.path.abspath(os.path.dirname(__file__))

# class BaseConfig:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

    ##### Flask-Mail configurations #####
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'infooveriq@gmail.com'
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    # MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopmentConfig(object):
    DEBUG = True
    

    
