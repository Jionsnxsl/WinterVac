# coding = utf-8

'''
    使用SQLight3
'''
import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("create table user (id varchar(20) PRIMARY KEY ,name VARCHAR(20))")
cursor.execute("INSERT INTO user(id, name) VALUES (3,\"jj\")")
print("affect row {0}".format(cursor.rowcount))
cursor.close()
conn.commit()
conn.close()

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("select * from user ")
data = cursor.fetchall()
print(data)
cursor.close()
conn.close()
