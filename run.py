# -*- coding:utf-8 -*-
from flask import current_app
from werkzeug.exceptions import HTTPException
from app import create_app
from app.base import db
from app.libs.error import APIException
from app.libs.error_code import ServerError
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app("develop")
CORS(app)


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        current_app.logger.error(e)
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


# 更新数据库
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
# if __name__ == '__main__':
#     app.run(host="192.168.43.226", port=5000, debug=True)
#     #app.run(host="172.16.11.11", port=5000, debug=True)
