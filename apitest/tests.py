# -*- coding:utf-8 -*-
#####################################
#作者：fin
#日期：2019年1月
#版本：autotestplat V1.1
#####################################
from django.test import TestCase

# Create your tests here.

from apitest.views import test,home,login
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import resolve
from django.urls import reverse
from django.http import HttpRequest


#class titlePageTest(TestCase):
#    def test_loginpage_returns_title_html(self):
#        request = HttpRequest()
#        response = login(request)
#        self.assertIn(b'<title>AutotestPlat</title>', response.content)

class contentTest(TestCase):
    def test_content_url_resolves_to_view(self):
        request = HttpRequest()
        response = login(request)
        self.assertIn(b'test1234567', response.content)

