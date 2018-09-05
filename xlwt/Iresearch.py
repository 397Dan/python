#usr/bin/python
#coding=utf-8

"""
写入excel的简单操作
"""

import urllib2
import xlwt
import time
import json
import os

channelData = {"art":"3","tv":"2"}
equData = {"mobile":"2"}
timeData = {
	"201803":62,
	"201802":61,
	"201801":60,
	"201712":59,
	"201711":58,
	"201710":57,
	"201709":56,
	"201708":55,
	"201707":54,
	"201706":53,
	"201705":52,
	"201704":51,
	"201703":50,
	"201702":49,
	"201701":48
}

class Iresearch:

	def __init__(self):
		self.workbook = xlwt.Workbook()
		self.worksheet = self.workbook.add_sheet('My Worksheet',cell_overwrite_ok=True)
		self.worksheet.write(0, 0, u'日期')  # 不带样式的写入
		self.worksheet.write(0, 1, u'电影名')  # 不带样式的写入
		self.worksheet.write(0, 2, u'票房(万)')  # 不带样式的写入
		self.worksheet.write(0, 3, u'releaseInfo')  # 不带样式的写入
		self.worksheet.write(0, 4, u'splitSumBoxInfo')  # 不带样式的写入
		self.worksheet.write(0, 5, u'splitBoxRate')  # 不带样式的写入
		self.worksheet.write(0, 6, u'splitBoxInfo')  # 不带样式的写入
		self.worksheet.write(0, 7, u'showInfo')  # 不带样式的写入
		self.worksheet.write(0, 8, u'showRate')  # 不带样式的写入
		self.worksheet.write(0, 9, u'avgShowView')  # 不带样式的写入
		self.worksheet.write(0, 10, u'splitAvgViewBox')  # 不带样式的写入
		# self.worksheet.write(0, 2, u'设备数')  # 不带样式的写入
		# self.worksheet.write(0, 3, u'设备数(万)')  # 不带样式的写入
		# self.worksheet.write(0, 4, u'月份')  # 不带样式的写入

	def getPageContent(self,url,delay=0):
		time.sleep(delay)
		res = urllib2.Request(url)
		response = urllib2.urlopen(res)
		content = response.read()
		return content

	def getUrls(self,channel,tool,time,page):
		self.isDirExists()
		baseUrl = "http://index.iresearch.com.cn/Video/GetDataList?classId=%s&deviceTypeId=%s&timeId=%s&pageIndex=%s"
		for i in range(timeData[time[0]],timeData[time[1]]+1):
			for j in range(page):
				url = baseUrl%(channelData[channel],equData[tool],i,j+1)
				content = self.getPageContent(url,1)
				pageDict = json.loads(content)
				if pageDict.has_key('List') and isinstance(pageDict['List'],list) and len(pageDict['List']) != 0:
					for num,k in enumerate(pageDict['List']):
						date = k['TimeName']
						name = k['mName']
						rank = j*20+(num+1)
						equCount = k['TimeData']
						equCountWan = k['UV']
						self.worksheet.write(rank,0,rank)
						self.worksheet.write(rank,1,name)
						self.worksheet.write(rank,2,equCount)
						self.worksheet.write(rank,3,equCountWan)
						self.worksheet.write(rank,4,date)
			dateName = list(timeData.keys())[list(timeData.values()).index(i)]
			self.workbook.save("Iresearch/"+dateName+"_"+channel+"_"+tool+".xls")
			print dateName+"已经写入"

	def getMaoyan(self):
		num = 0
		baseUrl = 'https://box.maoyan.com/promovie/api/box/second.json?beginDate=2018%s%s'
		for i in range(1,7):
			i = '0%s'%i if len(str(i)) == 1 else i
			for j in range(1,32):
				j = '0%s' % j if len(str(j)) == 1 else j
				url = baseUrl%(str(i),str(j))
				print url
				date = '2018%s%s'%(str(i),str(j))
				content = self.getPageContent(url,1)
				pageDict = json.loads(content)
				if pageDict['data'].has_key("list"):
					for n in pageDict['data']['list']:
						num += 1
						boxInfo = n['boxInfo']
						name = n['movieName']
						releaseInfo = n['releaseInfo']
						splitSumBoxInfo = n['splitSumBoxInfo']
						splitBoxRate = n['splitBoxRate']
						splitBoxInfo = n['splitBoxInfo']
						showInfo = n['showInfo']
						showRate = n['showRate']
						avgShowView = n['avgShowView']
						splitAvgViewBox = n['splitAvgViewBox']
						self.worksheet.write(num,0,date)
						self.worksheet.write(num,1,name)
						self.worksheet.write(num,2,boxInfo)
						self.worksheet.write(num,3,releaseInfo)
						self.worksheet.write(num,4,splitSumBoxInfo)
						self.worksheet.write(num,5,splitBoxRate)
						self.worksheet.write(num,6,splitBoxInfo)
						self.worksheet.write(num,7,showInfo)
						self.worksheet.write(num,8,showRate)
						self.worksheet.write(num,9,avgShowView)
						self.worksheet.write(num,10,splitAvgViewBox)
		self.workbook.save("BoxInfo.xls")

	def isDirExists(self):
		path = 'Iresearch/'
		if os.path.exists(path):
			pass
		else:
			os.makedirs(path)

if __name__ == '__main__':
	Iresearch().getMaoyan()
	# Iresearch().getUrls("tv","mobile",["201701","201803"],5)

