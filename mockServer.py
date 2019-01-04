#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: mockServer.py
@time: 2019/01/04
"""
import  web

#元组URL规则
urls = {
    '/','index',
}

class index:
    def GET(self):
        return 'hello word!'

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()