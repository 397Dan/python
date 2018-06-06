#usr/bin/python
#coding=utf-8
"""
	对来自一个迭代器的重复元素分组，只要相邻（所以大多需要sort（）排序），还可以提供另一个函数来执行元素的比较
"""

from itertools import *

def height_class(h):
    if h>180:
        return 'tall'
    elif h<160:
        return 'short'
    else:
        return 'middle'

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends,key = height_class)

for m,n in groupby(friends,key = height_class):
    print m
    print list(n)

#第二例

from itertools import groupby

def compress(data):
    return ((name, len(list(group))) for name, group in groupby(data))

def decompress(data):
    return (name * size for name, size in data)

print list(compress('get uuuuuuuuuuuuuuuuuuuuuuuup'))
c = compress('get uuuuuuuuuuuuuuuuuuuuuuuup')
print(''.join(decompress(c)))