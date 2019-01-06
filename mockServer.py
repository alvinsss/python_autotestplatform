#    -*- coding: utf-8 -*-
'''
@author: alvin
'''
""" Basic todo list using webpy 0.4 """
import web
from web.contrib.template import  render_jinja
import  os
import  pymysql
pymysql.install_as_MySQLdb()
import  sys

# ## Url mappings
urls = (
    '/index',     'index',
    '/apiget'   , 'apiget',
    '/apipost'   , 'apipost',
    '/jinjam'   ,  'jinjiaM',
    '/dbgetdata',  'dbget',
)
web.config.debug = True

# ## Templates 增加灵活度
app_root                            = os.path.dirname(__file__)
templates_htmlroot                  = os.path.join(app_root,'static/templates')
# templates_htmlroot_templates        = os.path.join(templates_htmlroot,'templates')
render =  render_jinja(templates_htmlroot)

class index():
    print("index fun")
    def GET(self):
        # return web.seeother('/templates/indexs.html')
        return web.seeother('/static/templates/index.html')


# http://127.0.0.1:8080/apiget?firstname=alvin&lastname=hailin
class apiget():
    def GET(self):
        firstname = web.input().firstname
        lastname  = web.input().lastname
        return firstname,lastname

class apipost():
    def POST(self):
        firstname = web.input().firstname
        lastname  = web.input().lastname
        return firstname,lastname

class jinjaM:
    def GET(self):
        return render.jinjam
        #返回jinjam.html

class dbget:
    print("db get data")
    def GET(self):
        # db = web.database(dbn="mysql",host="localhost",port="3306",user="qa",pw="qatest",db="test",charset='utf8')
        # res = db.query("select * from user")
        conn = pymysql.connect(host="localhost",user="qa",passwd="qatest",db="test")
        str1 = "aaa"
        cursor = conn.cursor()
        exec_sql = cursor.execute("select * from user")
        res = conn.commit()
        cursor.close()
        conn.close()
        return  res[0]


app = web.application(urls, globals())
if __name__ == '__main__':
    print("mock server starting ...")
    app.run()