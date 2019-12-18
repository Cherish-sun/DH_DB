from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from app.models import User_excel

Base = declarative_base()
host = '127.0.0.1'
user = 'root'
password = '123456'
port = 3306

# class Student(Base):
#     __tablename__ = 'student'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100))
#     age = Column(Integer)
#     address = Column(String(100))
# class User_excel(Base):
#     __tablename__ = 'user_excel'
#     id = Column(Integer, primary_key=True)
#     filename = Column(String(64), nullable=False)  # 文件名
#     path = Column(String(200), nullable=False, unique=True)  # 路径
#     fgroup = Column(String(60), nullable=True)  # 用来放文件的分组，后加字段
#     created_date = Column(DateTime, default=datetime.now)
#     user_id = Column(Integer, nullable=False)  # 用户id
#     user_name = Column(String(20), nullable=False)  # 用户名
#     role = Column(String(20), nullable=False)  # 岗位名
#     role_id = Column(Integer, nullable=False)  # 岗位id
#     department_id = Column(Integer, nullable=True)  # 部门id
#     department = Column(String(20), nullable=True)  # 部门
#     status_id = Column(Integer, ForeignKey("status.id"))
#     win_file_path = Column(String(200), nullable=True)
#     status = relationship("Status", back_populates="exceles")  # 状态id
#
#
# class Status(Base):
#     __tablename__ = 'status'
#     id = Column(Integer, primary_key=True)
#     status_name = Column(String(5), nullable=False)
#     created_date = Column(DateTime, default=datetime.now)
#     # 下面这个不是字段，是为了方便查询，反向查询，比如某一个状态下有多少个表，就可以利用这个区查询。
#     exceles = relationship("User_excel", back_populates="status")
# def update(session):
#     student1 = session.query(Student).filter(Student.id == 1001).one()
#     student1.name = 'test123'
#     session.commit()
#     student2 = session.query(Student).filter(Student.id == 1001).one()
#     print(student2.name)
#
#
# def delete(session):
#     session.query(Student).filter(Student.id == 1001).delete()
#     session.commit()
#
#
# def insert(session):
#     student1 = Student(id=1004, name='ling', age=28, address='shanxi')
#     session.add(student1)
#     session.commit()
#
#
# def count(session):
#     numnber = session.query(Student).filter().count()
#     print("total student is {0}".format(numnber))
#
#
# def groupBy(session):
#     groupByAge = session.query(Student).group_by(Student.age).all()
#     print(groupByAge)
#     for i in groupByAge:
#         print(i.id, i.name, i.age, i.address)
#
#
def orderBy(session):
    orderByAge = session.query(User_excel).order_by(User_excel.created_date.desc()).all()
    for x in orderByAge:
        print(x)


def main():
    user_id = 1
    user_name = 'job'
    user_job_id = 11
    user_role = 'safeperson'

    database = str(user_id) + "_" + user_name + "_" + str(user_job_id) + "_" + user_role
    url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(user, password, host, port, database)
    engine = create_engine(url)
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    # insert(session)
    # update(session)
    # delete(session)
    # count(session)
    # groupBy(session)
    orderBy(session)


if __name__ == '__main__':
    main()