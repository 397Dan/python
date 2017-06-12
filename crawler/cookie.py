# -*- coding: UTF-8 -*-
# !usr/bin/python
# coding = utf-8

import urllib2
import cookielib
import urllib

# # 保存在变量中
# cookie = cookielib.CookieJar()  #声明一个CookieJar对象实例来保存cookie
# handle = urllib2.HTTPCookieProcessor(cookie) #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# opener = urllib2.build_opener(handle) #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('https://www.baidu.com/')
# for item in cookie:
#     print '啊啊啊啊啊',item
#     print 'Name ='+item.name
#     print 'Value ='+item.value


# # 保存在文件中
# mycookie = cookielib.MozillaCookieJar() #声明一个MozillaCookieJar的类对象保存cookie(注意MozillaCookieJar的大小写问题)
# handler = urllib2.HTTPCookieProcessor(mycookie) #利用urllib2库中的HTTPCookieProcessor来声明一个处理cookie的处理器
# opener = urllib2.build_opener(handler) #利用handler来构造opener，opener的用法和urlopen()类似
# response1 = opener.open("http://www.baidu.com") #opener返回的一个应答对象response
# for item in mycookie:
#   print"name="+item.name
#   print"value="+item.value
# filename='mycookie.txt'#设定保存的文件名
# mycookie.save(filename,ignore_discard=True, ignore_expires=True)

#
# # 从文件中读取并访问
# 第一步先给出账户密码网址准备模拟登录
postdata = urllib.urlencode({
    'stuid': '760410476@qq.com',
    'pwd': '2336646.'  # 密码这里就不泄漏啦，嘿嘿嘿
})
loginUrl = 'http://www.baidu.com'  # 登录教务系统的URL，成绩查询网址

# 第二步模拟登陆并保存登录的cookie
filename = 'cookie.txt'  # 创建文本保存cookie
mycookie = cookielib.MozillaCookieJar(filename)  # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(mycookie))  # 定义这个opener，对象是cookie
result = opener.open(loginUrl,postdata)
for item in mycookie:
    print item
mycookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
gradeUrl = 'https://passport.baidu.com/center'  #只要是帐号密码一样的网址就可以， 请求访问成绩查询网址
result1 = opener.open(gradeUrl)
print result1.read()

