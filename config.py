# -*- coding: utf-8 -*-
import getpass
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # BASE
    WORKING_PATH = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir))
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
    CURRENT_USER = getpass.getuser()

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:passwd@host:port/db?charset=utf8"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = False

    # 确保在flask restful中jsondumps时中文的可读性
    RESTFUL_JSON = dict(ensure_ascii=False)


app_conf = Config()
