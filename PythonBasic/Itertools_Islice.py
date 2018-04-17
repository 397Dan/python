#!usr/bin/python
#coding=utf-8

"""
	python中添加迭代器以后 itertools覆盖了许多模式 islice tee groupby
	islice窗口迭代器
	返回一个运行在序列的子分组之上的迭代器  当需要抽取位于流中特定位置的数据时
"""

import itertools

def starting_at_five():
	value = raw_input().strip()
	while value != "":
		for el in itertools.islice(value.split(),4,None):
			yield el
		value = raw_input().strip()

iter = starting_at_five()
print iter.next()
print iter.next()
print iter.next()

# input 1 2 3 4 5 6 和input1 2 3 4 5 6 7 是两种效果 因为yield的机制