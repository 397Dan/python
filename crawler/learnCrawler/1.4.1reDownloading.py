#!usr/bin/python
#coding=utf-8

import urllib2
import re

class test():
    def reDownloading(self,url,user_agent='wswp',num=2):  # num为重新下载的次数
        print 'Downloading url:',url
        headers = {'User_agent':user_agent}
        request = urllib2.Request(url,headers=headers)
        try:
            html = urllib2.urlopen(request).read()
        except urllib2.URLError as e:           # 异常类型
            print 'Downloading erro:',e.reason
            html = None
            if num > 0 :
                if hasattr(e,'code') and 500 <= e.code <600:
                    return self.reDownloading(url,'wswp',num-1)
        print html
        return html

    def crawls_itemap(self,url):
        itemap = self.reDownloading(url)
        print itemap
        links = re.findall('<loc>(,*?)</loc>',itemap)
        for l in links:
            print l



if __name__ == '__main__':
    url = 'http://httpstat.us/500'
    #test().reDownloading(url)
    test().crawls_itemap('http://example.webscraping.com/stemap.xml')


