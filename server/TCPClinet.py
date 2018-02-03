#!usr/bin/python
#coding=utf-8
from socket import *

HOST = 'localhost'   # 同一台机器 所以用本机额 若用其他主机需要相应修改
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = raw_input('> ')
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data

tcpCliSock.close()