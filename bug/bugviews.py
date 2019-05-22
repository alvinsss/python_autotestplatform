# -*- coding:utf-8 -*-
#####################################
#作者：fin
#日期：2019年1月
#版本：autotestplat V1.1
#####################################
from django.shortcuts import render
from bug.models import Bug
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login

#bug管理
def bug_manage(request):
    username = request.session.get('user', '')
    bug_list = Bug.objects.all()
    bug_count = Bug.objects.all().count()  #ͳ��bug��
    paginator = Paginator(bug_list, 8)  #����paginator����,����ÿҳ��ʾ8����¼
    page = request.GET.get('page',1)  #��ȡ��ǰ��ҳ����,Ĭ��Ϊ��1ҳ
    currentPage=int(page)  #�ѻ�ȡ�ĵ�ǰҳ����ת������������
    try:
        bug_list = paginator.page(page)#��ȡ��ǰҳ�����ļ�¼�б�
    except PageNotAnInteger:
        bug_list = paginator.page(1)#��������ҳ��������������ʾ��1ҳ������
    except EmptyPage:
        bug_list = paginator.page(paginator.num_pages)#��������ҳ������ϵͳ��ҳ��������ʾ���һҳ������
    return render(request, "bug_manage.html", {"user": username,"bugs": bug_list,"bugcounts": bug_count}) #��ֵ����bugcounts�������

# ��������
@login_required
def bugsearch(request):
    username = request.session.get('user', '') # ��ȡ�������¼session
    search_bugname = request.GET.get("bugname", "")
    bug_list = Bug.objects.filter(bugname__icontains=search_bugname) 
    return render(request,'bug_manage.html', {"user": username,"bugs":bug_list})
