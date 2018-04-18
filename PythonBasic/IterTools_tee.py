#usr/bin/python
#coding=utf-8

"""
	tee:往返式迭代器。迭代器会消耗他处理的序列，并不会反向处理。tee提供了在一个序列上运行多个迭代器的模式，即：原始数据为一个序列，可以生成多个迭代器，并且分别参与运行
"""
import itertools
def with_head(iterable,headsize=1):
	a,b = itertools.tee(iterable)
	return list(itertools.islice(a,headsize)),b

print with_head(iter("1234"))
print with_head(iter("1234"),4)

# 用tee生成两个迭代器，第一个迭代器执行islice，第二个迭代器返回的是一个迭代器，可用在整个序列上