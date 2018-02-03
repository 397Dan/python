#!/usr/bin/python
#coding=utf-8

'''
	近似算法
	用途:获取精确时间太长
	判断优劣标准：1.速度有多快；2.得到的近似解与最优解的接近程度
'''


states_needs = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
final_stations = set()
while states_needs:
	states_cover = set()
	best_station = None
	for station,states_for_stations in stations.items():
		cover = states_for_stations & states_needs
		if len(cover) > len(states_cover):
			states_cover = cover
			best_station = station
	final_stations.add(best_station)
	states_needs =states_needs - states_cover
print final_stations

