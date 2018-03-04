# coding=utf-8

'''
TCP 编程
'''

import socket

# 创建一个socket，指定连接的协议是IPV4和TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接目标计算机，传入目标计算机的IP地址和端口号
s.connect(('www.sina.com.cn',80))
# 发送请求
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接受数据
# data = s.recv(1024)

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
s.close()

header, html = data.split(b'\r\n\r\n',1)
print(header.decode("utf-8"))

with open("sina.html","wb") as f:
    f.write(html)


'''
TCP 服务端
'''
import socket,threading,time
# 处理来自客户端的连接请求
def tcplink(sock,addr):
    print("Accept new connection from {addr[0]} : {addr[1]}".format(addr=addr))
    sock.send(b"Welcome!")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8") == "exit":
            break
        sock.send(("Hello %s!"%data.decode("utf-8")).encode("utf-8"))
    sock.close()
    print("Connection from {addr[0]} : {addr[1]} closed".format(addr=addr))

# 创建基于IPV4和TCP的socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 将socket绑定在某个IP上，并指定监听端口
s.bind(('127.0.0.1',9999))
# 最大监听数量（等待数量）
s.listen(10)
print("Waiting for connection....")

while True:
    # 接受来自客户端的请求，获取连接socket和IP
    sock, addr = s.accept()
    # 为到来的请求创建处理线程
    t = threading.Thread(target=tcplink,args=(sock, addr))
    t.start()





