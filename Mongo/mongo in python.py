#!usr/bin/python
#coding = utf-8

import pymongo

connection = pymongo.MongoClient()
tdb = connection.jikexueyuan
post_info = tdb.test

jike = {'name':'jike','age':'5','skill':'python'}
god = {'name': 'yuhuangdadi', 'age': 36000, 'skill': 'creatanything', 'other': 'wangmuniangniang'}
godslaver = {'name': 'yuelao', 'age': 'unknown', 'other': 'mengpo'}
post_info.insert(jike)
post_info.insert(jike)
post_info.insert(god)
post_info.insert(godslaver)


print 1