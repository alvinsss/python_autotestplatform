# -*- coding:utf-8 -*-
#####################################
#作者：fin
#日期：2019年1月
#版本：autotestplat V1.1
#####################################
from django.contrib import admin

from django.contrib import admin 

from webtest.models import Webcase,Webcasestep 


# Register your models here.


class WebcasestepAdmin(admin.TabularInline):

    list_display=['webcasename','webteststep','webtestobjname','webfindmethod','webevelement','weboptmethod','webassertdata',
'webtestresult','create_time','id','webcase']

    model = Webcasestep

    extra=1
 	



class WebcaseAdmin(admin.ModelAdmin):

    list_display = ['webcasename', 'webtestresult','create_time','id']

    inlines = [WebcasestepAdmin]	


admin.site.register(Webcase,WebcaseAdmin)

