# -*- coding: utf-8 -*-

import logging
from flask_cors import CORS

# from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config

import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

app = Flask(__name__)
app.secret_key = config.APP_SECRET_KEY
app.config["SECRET_KEY"] = config.APP_SECRET_KEY
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.debug = config.DEBUG

app.config["MAIL_USERNAME"] = config.MAIL_USERNAME
app.config["MAIL_PASSWORD"] = config.MAIL_PASSWORD
app.config["MAIL_DEFAULT_SENDER"] = config.MAIL_DEFAULT_SENDER
app.config["MAIL_SERVER"] = config.MAIL_SERVER
app.config["MAIL_PORT"] = config.MAIL_PORT

# csrf = CSRFProtect(app)
db = SQLAlchemy(app)
mail = Mail(app)
# enable CORS
CORS(app)

if not app.debug:
    logging.basicConfig(filename="error.log", level=logging.INFO, format="%(asctime)s %(message)s")
else:
    toolbar = DebugToolbarExtension(app)
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# custom jinja line delimeters
app.jinja_env.line_statement_prefix = "%"
app.jinja_env.line_comment_prefix = "##"

# register views
from chadevmonster.views import init_views

init_views(app)
