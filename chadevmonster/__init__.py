# -*- coding: utf-8 -*-

import logging
from flask_cors import CORS

# from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# import requests.packages.urllib3
# requests.packages.urllib3.disable_warnings()

from config import get_config


db = SQLAlchemy()
mail = Mail()


def create_app(testing=False, test_config=None):

    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        config = get_config(testing)
        app.config.from_object(config)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    mail.init_app(app)

    # enable CORS
    CORS(app)
    # csrf = CSRFProtect(app)

    if not app.debug:
        logging.basicConfig(filename="error.log", level=logging.INFO, format="%(asctime)s %(message)s")
    else:
        toolbar = DebugToolbarExtension(app)
        app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

    # custom jinja line delimeters
    app.jinja_env.line_statement_prefix = "%"
    app.jinja_env.line_comment_prefix = "##"

    # register views
    with app.app_context():
        from chadevmonster.views import init_views
        init_views(app)

        return app
