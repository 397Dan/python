#usr/bin/python
#coding=utf-8

import urllib2
import json

baseData = {
      "jobId": "ChannelSearch-2020-02-17",
      "priority": -10, # 任务优先级，数字越小优先级越高，可设成-99,正式版任务一般为0,1,2
      "version": "20200217-daily",
      "jobDuration": 0,#不用动
      "taskType": "drama",
      "duration": 1800,
      "data": [
        {
          "path": "daily-test/2020-02-17",
          "channelType": "tv",
          "endTime": 1581868800,  # 与endTime同为0 默认抓取前一天数据
          "startTime": 1581782400,
          "home_url": "",
          # "name": ""
        }
      ],
      "channel": "qq"
    }

class addTask():
    def main(self,jobId,version,channel,path,channelType,startTime,endTime,home_url):
        head = {'User-Agent': 'Yunduan-AddTask-POST'}
        # url = 'http://crawler-server.internal.enlightent.com:53248/addtask' # 正式版用53248
        url = 'http://crawler-server.internal.enlightent.com:53250/addtask' # 测试版用53250不入正式库
        baseData['jobId'] = jobId
        baseData['version'] = version  # 20200218-daily等
        baseData['channel'] = channel  # qq,iqiyi等
        baseData['data'] = [
            {
                "__module__": "YunduanUtils.TaskMakerData",
                "__class__": "DramaData",
                "num": ["zheng_pian"], # 只抓正片
                "danmu": 1,  # 1:不抓弹幕;0:抓168小时弹幕;2：抓取全部弹幕，3：仅保留基本信息，不保留弹幕内容
                "path": path,
                "channelType": channelType,
                "endTime": endTime,
                "startTime": startTime,
                "home_url": home_url,
            }
        ]
        data = json.dumps(baseData)
        req = urllib2.Request(url, data, headers=head)
        content = urllib2.urlopen(req, timeout=10).read()
        print content

if __name__ == '__main__':
    jobId = 'jobid_iqiyi_drama_2020-02-18_18-55-31_1c8c5'
    verson = '20200218-1-develop'
    channel = 'iqiyi'
    path = 'test/iqiyi_drama/20200218'
    channelType = 'animation'
    startTime = 0
    endTime = 0
    home_url = 'https://www.iqiyi.com/a_19rrhw8m9x.html'
    addTask().main(jobId,verson,channel,path,channelType,startTime,endTime,home_url)