#!usr/bin/python
#coding=utf-8

'''
增：sadd 删：srem
sismember:检查元素是否存在在集合里
scard：返回集合包含的数量
srandmember key-name [count] 从集合里随机返回一个或多个元素 count为正时随机元素不会重复 count为负时随机元素可能会重复
spop：随机删除集合中一个元素并返回
smove source-key dest-key item 如果集合source-key含有item元素 那么从前面的集合移除元素，并添加到后面的集合中 操作成功返回1，否则返回0
'''

import redis

conn = redis.Redis()

# print conn.sadd('set-key','a','b','c','d')  #>>>返回的是要添加进去的元素的长度 比如添加‘a’，‘b’，‘c'返回长度就是3
# print conn.srem('set-key','c','d')     #返回被移除元素的数量 有bug的时候可能返回布尔值
# print conn.scard('set-key')       #查看集合包含的元素数量
# print conn.smembers('set-key')  #获取集合包含的所有元素
# print conn.smove('set-key','set-key2','a')
# print conn.smove('set-key','set-key2','c')
# print conn.smembers('set-key2')

'''
sdiff  key-name [key-name...] 返回存在于第一个集合但是不存在于其他集合中的元素（差集运算）
sdiffstore dest-key key-name [key-name...] 将差集运算的结果存储到dest-key键里面
sinter key-name [key-name...]返回同时存在所有集合的元素（交集运算）
sinterstore dest-key key-name [key-name...]交集运算的记过存储到dest-key键里
sunion key-name [key-name...] 返回至少存在于一个集合的元素（并集运算）
sunionstore 同上类似
'''
conn.delete('skey1')
conn.delete('skey2')
print conn.sadd('skey1','a','b','c','d')
print conn.sadd('skey2','c','d','e','f')
print conn.sdiff('skey1','skey2')
print conn.sinter('skey1','skey2')
print conn.sunion('skey1','skey2')
