# -*- coding:utf-8 -*-
from logging.handlers import RotatingFileHandler
from flask import Flask
import logging

"""
    设置日志
"""
logging.basicConfig(level=logging.INFO)
file_log_handler = RotatingFileHandler("D:\\logs\\vm_server", encoding="UTF-8", maxBytes=1024 * 1024 * 100,
                                       backupCount=10)
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)



def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)
    #app.config.from_object('app.configs.config')
    register_blueprints(app)
    #register_plugin(app)
    return app
