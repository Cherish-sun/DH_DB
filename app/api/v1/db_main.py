# -*- coding:utf-8 -*-
import json
from flask import current_app
from app import constants
from app.configs.secure import FDFS_HOST, REDIS_STORE
from app.libs.UserInfo import user_db
import sqlalchemy
from flask import jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from app.configs.secure import MYSQL_USER, MYSQL_PORT, MYSQL_PASSWORD, MYSQL_HOST
from app.libs.error_code import ParameterException, NotFound, Success, DBERR
from app.libs.redprint import Redprint
from app.models import Status, User_excel, Base

api = Redprint('db')


@api.route('/create', methods=['POST'])
def create_db():
    # data = request.form
    # user_id = data.get("user_id")
    # user_name = data.get("username")
    # user_role = data.get("work")  # 这里和以前的角色内容一样，只不过名字变成了岗位
    # user_job_id = data.get("numVal")
    # user_department_id = data.get("department_id")
    user_id = 2
    user_name = 'job'
    user_job_id = 11
    user_role = 'safeperson'

    if not all(
            [user_id, user_name, user_job_id, user_role]):
        raise ParameterException(msg='用户参数不完整')

    database = str(user_id) + "_" + user_name + "_" + str(user_job_id) + "_" + user_role
    conn_str = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, database)
    engine = sqlalchemy.create_engine(conn_str, echo=True)

    if database_exists(engine.url):
        raise DBERR('数据库已存在')

    else:
        create_database(engine.url)
        Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    s = Status(status_name="报")
    s1 = Status(status_name="垃")
    s2 = Status(status_name="删")
    s3 = Status(status_name="收")
    s4 = Status(status_name="草")

    try:
        session.add_all([s, s1, s2, s3, s4])
        session.commit()
    except Exception as e:
        session.rollback()
        current_app.logger.error(e)
        return DBERR('创建数据库失败')
    return Success()


@api.route('/excel', methods=['POST'])
def excel():
    """
    根据前端传过来的用户信息，拼接用户库，并连接
    # data = request.form
    # user_id = data.get("user_id")
    # user_name = data.get("username")
    # user_role = data.get("work")  # 这里和以前的角色内容一样，只不过名字变成了岗位
    # user_job_id = data.get("numVal")
    """
    user_id = 1
    user_name = 'job'
    user_job_id = 11
    user_role = 'safeperson'

    if not all(
            [user_id, user_name, user_job_id, user_role]):
        raise ParameterException(msg='用户参数不完整')

    user_key = str(user_id) + "+" + user_name + "+" + str(user_job_id) + "+" + user_role

    ret = REDIS_STORE.get(user_key)
    if ret:
        current_app.logger.info("hit user excel info redis")
        return ret, 200, {"Content-Type": "application/json"}

    db_name = str(user_id) + "_" + user_name + "_" + str(user_job_id) + "_" + user_role

    session = user_db(db_name)
    exceles = session.query(User_excel).order_by(User_excel.created_date.desc()).all()
    if exceles:
        exceles_data = []
        for i in exceles:
            json_dict = {}
            json_dict["id"] = i.id
            json_dict["filename"] = i.filename
            json_dict["path"] = FDFS_HOST + i.path
            exceles_data.append(json_dict)
        resp_dict = dict(error_code=0, msg="OK", data=exceles_data)
        json_excel = json.dumps(resp_dict)
        REDIS_STORE.setex("{}".format(user_key), constants.USERT_EXCEL_LIST, json_excel)
    else:
        return NotFound()
    return json_excel, 200, {"Content-Type": "application/json"}


@api.route('/health', methods=['POST', 'GET'])
def vm_health():
    """
    健康检查
    :return:
    """
    return "ok", 200
