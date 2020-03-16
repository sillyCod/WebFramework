# -*- coding:utf-8 -*-
import logging
import os
import sys
from json import JSONEncoder
from logging.config import dictConfig

from flask import Flask
from flask_socketio import SocketIO
from mongoengine import connect
from redis import StrictRedis as Redis
from app.foundation import db

from config import Config
from logger_config import LoggerConfig

logger = logging.getLogger("web")

# db = SQLAlchemy()
socketio = SocketIO()
sys.path.append(Config.PROJECT_PATH)
redis_db = Redis()


def create_app(conf):
    # connect(Config.MONGODB["db"])
    app = Flask(__name__, template_folder=os.path.join(Config.WORKING_PATH, "templates"))
    app.config.from_object(conf)

    # configure_request(app)
    # async_mode = None
    # socketio.init_app(app, async_mode='eventlet')
    configure_error_handlers(app)
    configure_blueprints(app)
    dictConfig(LoggerConfig.dictConfig)

    print(app.url_map)

    return app


def configure_blueprints(app):
    from app.views.common_api import common_bp
    app.register_blueprint(common_bp)


class LogLevelFilter(logging.Filter):

    def __init__(self, name='', level=logging.DEBUG):
        super(LogLevelFilter, self).__init__(name)
        self.level = level

    def filter(self, record):
        return record.levelno <= self.level


# def configure_logging(app):
#     import os
#     from logging.handlers import RotatingFileHandler
#
#     formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(pathname)s - %(lineno)s - %(message)s')
#     if not os.path.isdir(app.config['LOG_PATH']):
#         os.makedirs(app.config['LOG_PATH'])
#
#     info_log_file = os.path.join(app.config['LOG_PATH'], 'info.log')
#     error_log_file = os.path.join(app.config['LOG_PATH'], 'error.log')
#     if not os.path.exists(info_log_file):
#         os.system(r'touch %s' % info_log_file)
#
#     if not os.path.exists(error_log_file):
#         os.system(r'touch %s' % error_log_file)
#
#     info_handler = RotatingFileHandler(filename=info_log_file,
#                                        maxBytes=app.config['LOG_FILE_MAX_BYTES'], backupCount=3, encoding='utf-8')
#     info_handler.setFormatter(formatter)
#     info_handler.setLevel(logging.INFO)
#     info_handler.addFilter(LogLevelFilter(name='infoFilter', level=logging.INFO))
#     app.logger.addHandler(info_handler)
#
#     error_handler = RotatingFileHandler(filename=error_log_file,
#                                         maxBytes=app.config['LOG_FILE_MAX_BYTES'], backupCount=3, encoding='utf-8')
#     error_handler.setFormatter(formatter)
#     error_handler.setLevel(logging.WARNING)
#     error_handler.addFilter(LogLevelFilter(name='errorFilter', level=logging.ERROR))
#     app.logger.addHandler(error_handler)
#
#
# def configure_request(app):
#     @app.after_request
#     def after_request(response):
#         if not request.headers.get('Origin'):
#             return
#
#         if request.headers.get('Origin') in app.config.get('ALLOW_ORIGINS'):
#             response.headers.add('Access-Control-Allow-Origin', request.headers.get('Origin'))
#             response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#             response.headers.add('Access-Control-Allow-Credentials', 'true')
#             response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,HEAD,OPTION')


def configure_error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(*args):
        return '404'

    @app.errorhandler(500)
    def error(*args):
        import traceback
        logger.error(traceback.format_exc())
        # app.mail.send_message("ALLLLL", body=traceback.format_exc(), sender="noreply-manuvision@ainnovation.com", recipients=["wangfusheng@ainnovation.com"])
        return "Things can go wrong will go wrong, so are the servers.", 500
