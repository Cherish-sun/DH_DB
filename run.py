# -*- coding:utf-8 -*-
from flask import current_app
from werkzeug.exceptions import HTTPException
from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError
from flask_cors import CORS

app = create_app()
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


if __name__ == '__main__':
    #manager.run()
    app.run(host="172.16.11.11", port=8080, debug=True)
