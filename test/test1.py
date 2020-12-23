#!usr/python/bin
#coding=utf-8

import copy

base = {
    "channel": "xigua",
    "data": {
      "channelType": "tv",
      "danmu": 1,
      "num": [
        0
      ],
      "repeat": 2,
      "url": {"pinyin":"dianying","filters":{"type":"电影","area":"全部地区","tag":"动作","sort":"综合排序"},"offset":0,"limit":18}
    },
    "taskType": "channel"
  }

tvArea = ["内地","港台地区","其他"]
tvTag = ["喜剧","爱情","家庭","战争","古装","动作","军旅","剧情",
          "悬疑","犯罪","伦理","都市","奇幻","武侠","历史","其他"]

movieArea = ['内地','中国香港','美国','日本','韩国','德国','英国','法国','加拿大','意大利',
            '澳大利亚','其他']
movieTag = ['动作','喜剧','爱情','惊悚','犯罪','恐怖','奇幻','科幻',
            '战争','家庭','古装','武侠','历史','动画','伦理','其他']

l = []
for i in tvTag:
    for j in tvArea:
        data = copy.deepcopy(base)
        data['data']['channelType'] = 'tv'
        data['data']['url']['filters']['area'] = j
        data['data']['url']['filters']['tag'] = i
        data['data']['url']['pinyin'] = "dianshiju"
        data['data']['url']['filters']['type'] = "电视剧"
        l.append(data)
import json
print len(l)
l1 = []
for i in movieTag:
    for j in movieArea:
        data = copy.deepcopy(base)
        data = copy.deepcopy(base)
        data['data']['channelType'] = 'movie'
        data['data']['url']['filters']['area'] = j
        data['data']['url']['filters']['tag'] = i
        data['data']['url']['pinyin'] = "dianying"
        data['data']['url']['filters']['type'] = "电影"
        l.append(data)
# print json.dumps(l1)

aArea = ['日韩','内地','欧美']
aTag = ['奇幻','科幻','励志','青春','爱情','喜剧','动作','其他']
l2 = []
for i in aTag:
    for j in aArea:
        data = copy.deepcopy(base)
        data = copy.deepcopy(base)
        data['data']['channelType'] = 'animation'
        data['data']['url']['filters']['area'] = j
        data['data']['url']['filters']['tag'] = i
        data['data']['url']['pinyin'] = "dongman"
        data['data']['url']['filters']['type'] = "动漫"
        l.append(data)
# print json.dumps(l2)
print len(l)
print json.dumps(l)

