# -*- coding:utf-8 -*-
#####################################
#作者：fin
#日期：2019年1月
#版本：autotestplat V1.1
#####################################
from django.contrib import admin

from apitest.models import Apitest, Apistep, Apis
from product.models import Product

# Register your models here.


class ApistepAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','apitest']
    model = Apistep
    extra=1

class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname', 'apitester','apitestresult','create_time','id']
    inlines = [ApistepAdmin]
    
class ApisAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','product']

admin.site.register(Apitest,ApitestAdmin)
admin.site.register(Apis)

admin.site.site_title = 'autotestplat'
admin.site.site_header = 'autotestplat'
