import os
import sys
from app import app
import logging
from logging.handlers import RotatingFileHandler

def not_exist_makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def init_app(app, logName):
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    )
    debug_log = os.path.join(app.root_path, 'logs/%s_debug.log'% logName)
    not_exist_makedirs(os.path.dirname(debug_log))

    debug_file_handler = RotatingFileHandler(
        debug_log, maxBytes=100000, backupCount=10
    )

    debug_file_handler.setLevel(logging.INFO)
    debug_file_handler.setFormatter(formatter)
    app.logger.addHandler(debug_file_handler)

    error_log = os.path.join(app.root_path, 'logs/%s_error.log'% logName)
    not_exist_makedirs(os.path.dirname(error_log))
    error_file_handler = RotatingFileHandler(
        error_log, maxBytes=100000, backupCount=10
    )
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)

    app.logger.setLevel(logging.DEBUG)
