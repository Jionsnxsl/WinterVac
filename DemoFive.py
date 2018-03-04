# coding : utf-8

'''
    MYSQL 的 ORM 了解
'''

from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 初始化数据库连接
engin = create_engine('mysql+mysqlconnector://root:admin@localhost:3306/test')

# 创建对象的基类（SqlORM 基类）
Base = declarative_base()

# 定义数据库对象 userinfo
class Userinfo(Base):
    # 表的名字
    __tablename__ = "userinfo"

    # 表的结构
    username = Column(String(20),primary_key=True)
    password = Column(String(20))


# 创建DBSession类型，注意这里返回的Class
DBSession = sessionmaker(bind=engin)

# 创建session对象，session 可视为当前数据库的连接
session = DBSession()

# # 创建Userinfo对象
# new_info = Userinfo(username="orm",password="admin")
#
# session.add(new_info)
# session.commit()
# session.close()

session = DBSession()
user_info = session.query(Userinfo).order_by(Userinfo.username)
user_info = session.query(Userinfo).filter_by(username = "jj")


for u in user_info:
    print(u.username,"----",u.password)

session.query(Userinfo).filter(Userinfo.username == "jj").delete()
session.commit()

session.close()

# 定义一个字段
zengjia = User(id=2, name='sbliuyao')
# 添加字段
session.add(zengjia)
# 添加多个字段
session.add_all([
    User(id=3, name='sbyao'),
    User(id=4, name='liuyao')])
#提交以上操作
session.commit()

#删除user表，id大于2的字段
session.query(User).filter(User.id > 2).delete()
session.commit()

#user表里的id等于2的字段修改为id=6
session.query(User).filter(User.id == 2).update({'id' : 6})
session.commit()

for instance in session.query(Userinfo).order_by(Userinfo.id):
    print(instance.id, instance.name)

for name, id in session.query(Userinfo.id, Userinfo.name):
     print(id, name)

