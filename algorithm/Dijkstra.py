#!usr/bin/python
#coding = utf-8

# 图转成dict   这是一种麻烦不现实的建法 留心以后学的过程中 复杂模型怎么建立
graph = {}
graph['musicBook'] = {}
graph['musicBook']['poster'] = 0
graph['musicBook']['cd'] = 5
graph['poster'] = {}
graph['poster']['guitar'] = 30
graph['poster']['drum'] = 35
graph['cd'] = {}
graph['cd']['drum'] = 20
graph['guitar'] = {}
graph['guitar']['piano'] = 20
graph['drum'] = {}
graph['drum']['piano'] = 10

print graph


