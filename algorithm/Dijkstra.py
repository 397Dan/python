#!/usr/bin/python
#coding=utf-8

import sys

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
graph['piano'] = {}

inf = float("inf")
cost = {}
cost["poster"] = 0
cost["cd"] = 5
cost["guitar"] = inf
cost["drum"] = inf
cost["piano"] = inf

parent = {}
parent["poster"]="musicBook"
parent["cd"] = "musicBook"

processed = []

def lowerCost(costs,processed):
	# 遍历costs字典 找出路径最短的节点
	lower_cost = float("inf")
	lower_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lower_cost and node not in processed:
			lower_cost = cost
			lower_cost_node = node
	return lower_cost_node

def Dijkstra(costs,graph,parent,processed):
	node = lowerCost(costs,processed)   	# 取出路径最短的节点
	while node is not None:		#
		cost = costs[node]		# 当前节点的花费
		neighbors = graph[node]		# 当前节点的邻居，从graph取出，所以graph的建立是在每个节点的基础上，具备一条边和两个点
		for n in neighbors.keys():	# 遍历当前节点的邻居
			new_cost = cost+neighbors[n]		# 计算邻居的最新花费：到当前节点花费+当前节点到邻居的花费。 所以创建costs字典的时候 要添加全部节点的花费，已知的为具体数字，未知的为无穷大
			if costs[n]>new_cost:
				costs[n] = new_cost		# 更新costs表中邻居的花费
				parent[n] = node		# 更新parent表中邻居的父节点为当前节点，所以parent表中，每个节点都要有父节点，未知的为:None
		processed.append(node)
		node = lowerCost(costs,processed)

def p(arg,parent):
	arg = parent[arg]
	return arg

def main(start,end):
	Dijkstra(cost, graph, parent, processed)
	arg = end
	l = []
	while True:
		if arg == start:
			print "结束了"
			break
		else:
			arg = p(arg, parent)
			l.append(arg)
	print l[::-1]
	print cost[end]

main("musicBook","piano")





