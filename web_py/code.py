#!/usr/bin/python
#coding=UTF-8

import web

urls = (
  '/', 'index'    )


class index:
    def GET(self):
        print "Hello, world!"
web.webapi.internalerror = web.debugerror
if __name__ == "__main__":
    app = web.application(urls, globals(),web.s)
    app.run()