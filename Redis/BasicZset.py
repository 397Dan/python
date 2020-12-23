#!usr/python/bin
#coding=utf-8

import redis

conn = redis.Redis()

conn.delete('zset-key')
print conn.zadd('zset-key','a',3,'b',2,'c',1) # python先输入成员后输入分值，这跟redis先输入分值后输入成员的做法相反
print conn.zcard('zset-key')
print conn.zincrby('zset-key','c',4) # 排名从0开始
print conn.zrange('zset-key',0,-1,withscores=True)
print conn.zscore('zset-key','b')
print conn.zrank('zset-key','c')
print conn.zcount('zset-key',0,3)   #统计指定范围内元素的数量
print conn.zrem('zset-key','b')
print conn.zrange('zset-key',0,-1,withscores=True)