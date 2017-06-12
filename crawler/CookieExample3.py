# -*- coding: UTF-8 -*-
# !usr/bin/python

import time
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
}
url = 'https://www.zhihu.com'


def kill_captcha(data):
    with open('1.gif', 'wb') as fp:
        fp.write(data)
    return input('captcha : ')


def login(username, password, kill_captcha):
    session = requests.session()
    _xsrf = session.get(url+'/#signin', headers=headers).cookies['_xsrf']
    captcha_content = session.get(url+'/captcha.gif?r=%d&type=login' % (time.time() * 1000), headers=headers).content

    data = {
        '_xsrf': _xsrf,
        'password': password,
        'captcha': kill_captcha(captcha_content),
        'email': username,
        'remember_me': 'true' # 字典的键值对顺序可以随机
    }

    resp = session.post(url+'/login/email', data=data, headers=headers).text
    # 登录成功
    assert r'\u767b\u5f55\u6210\u529f' in resp
    return session


if __name__ == '__main__':
    session = login('7604104762qq.com', '2336646.', kill_captcha)
    page = session.get(url, headers=headers).text
    soup = BeautifulSoup(page, 'lxml').findAll('a', {'class': 'question_link'})
    for s in soup:
        print(s.get('href'))
