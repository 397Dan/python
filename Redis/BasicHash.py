#!usr/python/bin
#coding=utf-8

'''
hmget key-name key [key...] 从散列里获取一个或多个键的值
hmset key-name key value [key value...] 为散列里面的一个或多个键设置值
hdel hdel key-name key [key...] 删除散列里一个或多个键值对 返回成功找到并删除的键值对的数量
hlen key-name 返回散列包含的键值对的数量
'''

import redis

conn = redis.Redis()

# conn.delete('hash-key')
# print conn.hmset('hash-key',{'k1':'v1','k2':'v2','k3':'v3'})  # m是more的意思 hset是单参数版本
# print conn.hmget('hash-key',{'k2','k3'})
# print conn.hlen('hash-key')
# print conn.hdel('hash-key','k1','k3') # hdel可以删除多个 所以没有hmdel

conn.delete('hash-key2')
print conn.hmset('hash-key2',{'short':'hello','long':1000*'1'})
print conn.hkeys('hash-key2')
print conn.hexists('hash-key2','num')
print conn.hincrby('hash-key2','num') # 和字符串一样，对散列中尚未存在的键执行自赠操作redis会将键的值当作0处理
print conn.hexists('hash-key2','num')
