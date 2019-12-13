from app.libs.error import APIException


class ParameterException(APIException):
    code = 200
    msg = '参数无效'
    error_code = 1000


class Success(APIException):
    code = 200
    msg = '操作成功'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = '服务器发生未知错误'
    error_code = 999


class NotFound(APIException):
    code = 400
    msg = '系统资源没有找到'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = '授权失败'
    error_code = 1005


class Forbidden(APIException):
    code = 403
    msg = '禁止访问'
    error_code = 1004


class DBERR(APIException):
    code = 404
    msg = '获取数据失败'
    error_code = 1003


class NODATA(APIException):
    msg = '查询无数据'
    error_code = 4002
