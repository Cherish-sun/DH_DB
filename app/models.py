from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User_excel(Base):
    __tablename__ = 'user_excel'
    id = Column(Integer, primary_key=True)
    filename = Column(String(64), nullable=False)  # 文件名
    path = Column(String(200), nullable=False, unique=True)  # 路径
    fgroup = Column(String(60), nullable=True)  # 用来放文件的分组，后加字段
    created_date = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, nullable=False)  # 用户id
    user_name = Column(String(20), nullable=False)  # 用户名
    role = Column(String(20), nullable=False)  # 岗位名
    role_id = Column(Integer, nullable=False)  # 岗位id
    department_id = Column(Integer, nullable=True)  # 部门id
    department = Column(String(20), nullable=True)  # 部门
    status_id = Column(Integer, ForeignKey("status.id"))
    win_file_path = Column(String(200), nullable=True)
    status = relationship("Status", back_populates="exceles")  # 状态id


class Vm_last_status(Base):
    __tablename__ = 'vm_latest_status'
    id = Column(Integer, primary_key=True)
    filename = Column(String(64), nullable=False)
    path = Column(String(256), nullable=False, unique=True)
    created_date = Column(DateTime, default=datetime.now)
    deleted = Column(Integer, default=0, nullable=False)
    user_id = Column(Integer, nullable=False)
    user_name = Column(String(20), nullable=False)
    role = Column(String(20), nullable=True)
    role_id = Column(Integer, nullable=True)
    department_id = Column(Integer, nullable=True)
    department = Column(String(20), nullable=True)
    leader = Column(String(20), nullable=True)

    @property
    def to_status_dict(self):
        """将基本信息转换为字典数据"""
        to_status_dict = {
            "path": self.path
        }
        return to_status_dict


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    status_name = Column(String(5), nullable=False)
    created_date = Column(DateTime, default=datetime.now)
    # 下面这个不是字段，是为了方便查询，反向查询，比如某一个状态下有多少个表，就可以利用这个区查询。
    exceles = relationship("User_excel", back_populates="status")
