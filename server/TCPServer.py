#!usr/bin/python
#coding=utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024   #缓存
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM) # 创建服务器套接字
tcpSerSock.bind(ADDR)					# 套接字与地址绑定
tcpSerSock.listen(5)					# 监听链接

while True:								# 服务器无限循环
	print "waiting for connection..."
	tcpCliSock,addr = tcpSerSock.accept()	# 接受客户端链接
	print '...connected from:',addr

	while True:								# 通信循环
		data = tcpCliSock.recv(BUFSIZ)		# 对话（接受recv()/发送send()）
		if not data:
			break
		print addr,data
		tcpCliSock.send('[%s] %s'%(ctime(),data))

	tcpCliSock.close()						# 关闭客户端套接字
tcpSerSock.close()							# 关闭服务器套接字（可选）