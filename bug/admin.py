# -*- coding:utf-8 -*-
#####################################
#���ߣ��޻ԡ��Զ���ƽ̨���Կ�������
#���ڣ�2018��1��
#�汾��autotestplat V1.1
#####################################
from django.contrib import admin
from bug.models import Bug

class BugAdmin(admin.ModelAdmin):
    list_display = ['bugname ', 'bugdetail ', ' bugstatus', ' buglevel', ' bugcreater', ' bugassign', 'create_time','id']

admin.site.register(Bug)  # ��bug����ģ��ע�ᵽdjango admin��̨������ʾ

