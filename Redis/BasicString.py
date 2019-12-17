#!usr/bin/python
#coding=utf-8
'''
redis数据结构(5):string(字符串)，list(列表)，set(集合)，hash(散列)，zset(有序集合)
>set hello world
OK
>get hello
"world"
>del hello
(integer)1
>get hello
(nil)
incr key-name    键存储的值加1
decr key-name    键存储的值减1
incrby key-name amount  键存储的值加上整数amount
decrby key-name amount  键存储的值减去整数位amount
incrbyfloat key-name amount 键存储的值加上浮点数  redis2.6以上版本可用
'''
import redis

conn = redis.Redis()

# # 1
# conn.delete('key')
# conn.get('key') #>>>None    #尝试获取一个不存在的值会获得None
# conn.incr('key')   #>>>1  #可以对不存在的键执行自增操作
# conn.incr('key',15)  # >>>16
# conn.decr('key',5)  # >>>11
# conn.get('key')   # >>>'11'  # 返回的是字符串
# conn.set('key','13') # True  # 设置键值的时候输入字符串 只要是能被解释为整数就可以当做整数
# print conn.incr('key') # >>>14

# #2
# conn.delete('new-string-key')
# print conn.append('new-string-key','hello ')
# print conn.append('new-string-key','world!')
# print conn.substr('new-string-key',3,7)
# print conn.setrange('new-string-key',0,'i')  # 不是添加 是修改
# print conn.get('new-string-key')
# print conn.setrange('new-string-key',11,',how are you') # 除了更改还能增长字符串
# print conn.get('new-string-key')
# conn.delete('another-key')
# print conn.setbit('another-key',2,1)  #二进制 偏移量为2的设置为1
# print conn.get('another-key')
# print conn.setbit('another-key',7,1)  # 二进制 偏移量为7的位置设置为1  则another-key为33 即‘？’
# print conn.get('another-key')






