# -*- coding:utf-8 -*-
from .app import Flask
from logging.handlers import RotatingFileHandler
from .app import Flask
import logging
from app.config.config import config_map
"""
    设置日志
"""
logging.basicConfig(level=logging.INFO)
file_log_handler = RotatingFileHandler("D:\\logs\\vm_server", encoding="UTF-8", maxBytes=1024 * 1024 * 100,
                                       backupCount=10)
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)


def register_plugin(app):
    from app.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app(config_name):
    app = Flask(__name__)
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    register_blueprints(app)
    register_plugin(app)
    return app
