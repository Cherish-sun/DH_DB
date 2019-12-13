# -*- coding:utf-8 -*-
from flask import jsonify, current_app
from app.config import secure
from app.libs.UserInfo import UserInfo
from app.libs.redprint import Redprint
from app.config.setting import REDIS_STORE
from app.models import *
api = Redprint('vm')


@api.route('/working')
def vm_working():
    """
        接收用戶信息提醒, 开始工作
    """
    user_infos = None
    try:
        user_infos = REDIS_STORE.get(secure.CURRENT_IP)

    except Exception as e:
        current_app.logger.error(e)
    """
        1、初始化用户信息，拼接库名
        2、查库，下载用户文件
        3、启动文件监控（新建，修改，删除）
        4、退出虚拟机（文件入库）
    """
    u = User_excel.query.all()
    print(u)
    print(user_infos)
    user = eval(user_infos)
    payload = user.get("payload")
    user_name = user.get("user_name")
    user_id = user.get("user_id")
    UserInfo(payload, user_id, user_name)
    # redis_store.delete(secure.CURRENT_IP)
    # print('刪除成功')
    res = {'code': 200}
    return jsonify(res)


@api.route('/exit')
def vm_exit():
    pass


@api.route('/health', methods=['POST', 'GET'])
def vm_health():
    """
    健康检查
    :return:
    """
    return "ok", 200
