# -*- coding: utf-8 -*-

import os
import config
from chadevmonster.errors import ConfigVarNotFoundError

"""Set up config variables.

If environment variable APP_SETTINGS is set to dev and the config/dev.py
file exists then use that file as config settings, otherwise pull in settings from the production environment
"""

if os.environ.get("ENVIRONMENT") == "dev":
    try:
        import config.dev as config  # config/dev.py
    except:
        raise EnvironmentError("Please create config/dev.py")
else:
    # production server environment variables
    import config.prod as config  # config/prod.py

    config.DEBUG = False


config.USER_APP_NAME = "chadevmonster"
config.APP_NAME = "chadevmonster"

required_config_vars = [config.APP_SECRET_KEY, config.DEBUG, config.PORT]

try:
    any(required_config_vars) is None
except Exception as e:
    missing_var = e.message.split()[-1]
    raise ConfigVarNotFoundError(missing_var)


class BaseConfig(object):
    """Base configuration."""

    SECRET_KEY = "my_precious"
    DEBUG = False


class TestingConfig(BaseConfig):
    """Testing configuration."""

    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    TESTING = True
    SECRET_KEY = "my_precious"
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
