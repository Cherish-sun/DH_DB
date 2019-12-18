import time
import sqlalchemy
from flask import current_app
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists
from app.libs.error_code import NotFound
from app.configs.secure import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD,MYSQL_PORT


def user_db(db_name):
    conn_str = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, db_name)
    engine = sqlalchemy.create_engine(conn_str, echo=True)

    if database_exists(engine.url):
        db_engine = engine.url
        with open('./record', 'a+') as f:
            f.write(time.strftime('%Y-%m-%d %H:%M:%S  ') + str(db_engine))
            f.write('\n')
        DBsession = sessionmaker(bind=engine)
        session = DBsession()
        return session
    else:
        current_app.logger.error('{}:该用户数据库不存在'.format(db_name))
        return NotFound(msg='用户库未创建')
