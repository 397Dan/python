#!usr/bin/python
#coding=utf-8

import requests
import cookielib
import re
import time


agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
headers = {
    'User-Agent':agent
}
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='CookieExample1')
try:
    session.cookies.load(ignore_discard=True)
except:
    print "Cookie 未能加载"
# 获取_xsrf
def getXsrf():
    url = 'http://www.zhihu.com'
    response = session.get(url,headers = headers)
    content = response.text
    pattern = re.compile(r'name="_xsrf" value="(.+?)"/>')
    m = pattern.search(content)
    _xsrf = ''
    if m is not None:
        _xsrf = m.group(1)
    return _xsrf

def getCaptcha():
    captcha_url = 'http://www.zhihu.com/captcha.gif?r=%s'%str(time.time()*1000)
    r = session.get(captcha_url,headers = headers)
    with open('captcha.jpg','wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print captcha_url
    captcha = raw_input('captcha:')
    return captcha

def Login():
    url = 'http://www.zhihu.com/login/phone_num'
    captcha = getCaptcha()
    data = {
        '_xsrf':getXsrf(),
        'password':'2336646.',
        'phone_num':'17710515207',
    }
    data['captcha']=captcha
    page = session.post(url,data=data,headers = headers)
    content = page.text
    print content
    session.cookies.save()

if __name__ == "__main__":
    Login()
