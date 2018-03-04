# coding : utf-8

'''
    操作MySQL
'''

import pymysql

conn = pymysql.connect(host="localhost", user='root', passwd='admin', db='test')
cursor = conn.cursor()
cursor.execute("select * from userinfo")
data = cursor.fetchall()
print("username    password")
for name,pwd in data:
    print(name,"      ",pwd)

cursor.execute("insert into userinfo(username, password) VALUES ('python','admin')")
conn.commit()
cursor.close()
conn.close()