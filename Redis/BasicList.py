#!usr/bin/python
#coding=utf-8

import redis

conn = redis.Redis()

# 1 阻塞 brpoplpush
conn.delete('list')
conn.delete('list2')
conn.delete('list3')
conn.rpush('list','item1')
conn.rpush('list','item2')
conn.rpush('list2','item3')
conn.brpoplpush('list3','list',10)  # 当list3为空的时候会延迟10秒等待list3有值,延迟结束后list3依旧为空 list也保持原样
print conn.lrange('list3',0,-1)  #>>>[]
print conn.lrange('list',0,-1)   #>>> ['item1', 'item2']

conn.brpoplpush('list2','list',10)  # 不被阻塞 不延迟 直接出结果
print conn.lrange('list',0,-1)