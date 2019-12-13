from datetime import datetime
from app.base import Base, db
from sqlalchemy import Integer, String, DateTime, ForeignKey


class User_excel(Base):
    '''用户文件表'''
    __tablename__ = 'user_excel'

    id = db.Column(Integer, primary_key=True)
    filename = db.Column(String(64), nullable=False)
    path = db.Column(String(200), nullable=False, unique=True)
    fgroup = db.Column(String(60), nullable=False)  # 用来放文件的分组，后加字段
    created_date = db.Column(DateTime, default=datetime.utcnow)
    deleted = db.Column(Integer, default=0, nullable=False)
    user_id = db.Column(Integer, nullable=False)
    user_name = db.Column(String(20), nullable=False)
    role = db.Column(String(20), nullable=False)
    role_id = db.Column(Integer, nullable=False)
    department_id = db.Column(Integer, nullable=True)
    department = db.Column(String(20), nullable=True)
    read = db.Column(Integer, nullable=True)
    any = db.Column(String(20), nullable=True)
    status_id = db.Column(Integer, ForeignKey("status.id"))
    status = db.relationship("Status", back_populates="exceles")


class Vm_last_status(Base):
    '''用户最后一次状态表'''
    __tablename__ = 'vm_latest_status'
    id = db.Column(Integer, primary_key=True)
    filename = db.Column(String(64), nullable=False)
    path = db.Column(String(256), nullable=False, unique=True)
    created_date = db.Column(DateTime, default=datetime.utcnow)
    deleted = db.Column(Integer, default=0, nullable=False)
    user_id = db.Column(Integer, nullable=False)
    user_name = db.Column(String(20), nullable=False)
    role = db.Column(String(20), nullable=True)
    role_id = db.Column(Integer, nullable=False)
    department_id = db.Column(Integer, nullable=True)
    department = db.Column(String(20), nullable=True)
    read = db.Column(Integer, nullable=True)
    leader = db.Column(String(20), nullable=True)


class Status(Base):
    '''
    状态表
    '''
    __tablename__ = 'status'

    id = db.Column(Integer, primary_key=True)
    status_name = db.Column(String(5), nullable=False)
    # 下面这个不是字段，是为了方便查询，反向查询，比如某一个状态下有多少个表，就可以利用这个区查询。
    exceles = db.relationship("User_excel", back_populates="status")
