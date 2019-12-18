from app.libs.UserInfo import user_db

"""
    mysql初始化连接配置
    1、根据用户信息，查（redis）是否存在db，如果没有则创建，有的话，直接连接
# """
db = user_db()
current_db = db.get('db_name')
if current_db:
    print('正在连接数据库：', db)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/9_caiwu_111_person?charset=utf8'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
else:
    print('出错了！')

