# -*- coding: utf-8 -*-
from .base import *

ENV = 'testing'

SECRET_KEY = "some secret key"
SQLALCHEMY_DATABASE_URI = "sqlite://"
PORT = 5000
DEBUG = True
TESTING = True

# running in test environment, use gmail account below
MAIL_USERNAME = "email@gmail.com"
MAIL_PASSWORD = "password"
MAIL_SERVER = "smtp.host.org"
MAIL_PORT = 587
MAIL_DEFAULT_SENDER = "SiteName <info@sitename.com>"

# logging
LOGGING_ON = True
PRINTLOG = False
