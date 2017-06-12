# !usr/bin/python
# coding = utf-8

import time
import requests
import urllib2
import urllib
import re

def login():
    _xsrf= ''
    agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
    headers = {
        'User-Agent':agent
    }
    res = urllib2.Request('https://www.zhihu.com/#signin',headers = headers)
    response = urllib2.urlopen(res)
    content = response.read()
    pattern = re.compile(r'name="_xsrf" value="(.+?)"/>')
    m = pattern.search(content)
    uuu = 'http://www.zhihu.com/captcha.gif?r=%s&type=login' % str(int(time.time() * 100))
    print uuu
    captcha = raw_input('capture:')
    if m is not None:
        _xsrf = m.group(1)
    value = {
        '_xsrf':_xsrf,
        'password':'2336646.',
        'phone_num':'17710515207',
        'captcha':captcha
    }

    data = urllib.urlencode(value)
    res1 = urllib2.Request('http://www.zhihu.com/login/phone_num',data)
    response1 = urllib2.urlopen(res1)
    content1 = response1.read()
    print content1

if __name__ == '__main__':
   login()
