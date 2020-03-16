# -*- coding: utf-8 -*-
# time: 2019/11/23 下午3:49
import logging
import ssl

from config import Config


class LogLevelFilter(logging.Filter):

    def __init__(self, name='', level=logging.DEBUG):
        super(LogLevelFilter, self).__init__(name)
        self.level = level

    def filter(self, record):
        ret = record.levelno < self.level
        return ret


class LoggerConfig:
    """
    日志文件配置
    """
    dictConfig = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {'format': '%(asctime)s - %(name)s - %(levelname)s - '
                                   '%(message)s - [in %(pathname)s:%(lineno)d]'},
            'short': {'format': '%(message)s'},
            # 'test_extra': {'format': '%(message)s - %(ip)s'}
        },
        'filters': {
            'no_error_filter': {
                '()': LogLevelFilter,
                'name': 'no_error',
                'level': logging.ERROR,
            },

            'no_info_filter': {
                '()': LogLevelFilter,
                'name': 'no_info',
                'level': logging.INFO,
            }
        },
        'handlers': {
            'file_debug': {
                'level': 'DEBUG',
                'filters': ['no_info_filter'],
                'formatter': 'standard',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/common/debug.log',
                'maxBytes': 10 * 1024 * 1024,
                'backupCount': 10
            },
            'file_info': {
                'level': 'INFO',
                'filters': ['no_error_filter'],
                'formatter': 'standard',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/common/info.log',
                'maxBytes': 10 * 1024 * 1024,
                'backupCount': 10
            },

            'file_error': {
                'level': 'ERROR',
                'formatter': 'standard',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/common/error.log',
                'maxBytes': 10 * 1024 * 1024,
                'backupCount': 10
            },
            'console': {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
            },

            'debug': {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler'
            },

        },
        'loggers': {
            'web': {
                'handlers': ['console', 'file_debug', 'file_info', 'file_error', "debug"],
                'level': 'DEBUG',
                'propagate': True},

            'werkzeug': {'propagate': True},

            'web.model': {
                'handlers': ['debug'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'web.view': {
                'handlers': ['debug'],
                'level': 'DEBUG',
                'propagate': False,
            },

            'web.sqltime': {
                'handlers': ['debug'],
                'level': 'INFO',
                'propagate': False
            },
            'task': {
                'handlers': ['console', 'file_debug', 'file_info', 'file_error'],
                'level': 'DEBUG',
                'propagate': True
            },
            'performance': {
                'handlers': ['console', 'file_debug', 'file_info', 'file_error', "debug"],
                'level': 'DEBUG',
                'propagate': True},
        },
        # 'root': { 'level': 'DEBUG', 'handlers': ['console'] }
    }
