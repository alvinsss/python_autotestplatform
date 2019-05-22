# -*- coding:utf-8 -*-
#####################################
#作者：fin
#日期：2019年1月
#版本：autotestplat V1.1
#####################################
import requests, time, sys, re
import urllib, zlib 
import pymysql
import unittest
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from apitest.celery import app
from time import sleep
import os
from appium import webdriver

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                           
)

global driver

@app.task    
def appauto_testcase(self):            #app例
    print("appauto_testcase")
    # 读取设备 id
    read_DeviceId = list( os.popen( 'adb devices' ).readlines() )
    # 读取设备系统版本号
    device_Android_Version = list( os.popen( 'adb shell getprop ro.build.version.release' ).readlines() )
    device_Id = read_DeviceId[1].split( '\t' )[0]
    print ("device_Android_Version",device_Android_Version)
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = device_Id
    desired_caps['appPackage'] = 'com.android.calculator2'
    desired_caps['appActivity'] = '.Calculator'
    time.sleep(3)
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(3)
    print("webdriver.Remote is ok!")
    sql="SELECT id,appfindmethod,appevelement,appoptmethod,appassertdata,`apptestresult` from apptest_appcasestep where apptest_appcasestep.Appcase_id=1 ORDER BY id ASC " 
    coon = pymysql.connect(user='qa',passwd='qatest',db='autotest',port=3306,host='127.0.0.1',charset='utf8')
    cursor = coon.cursor()
    aa=cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:   
        case_list = []
        case_list.append(ii)
        apptestcase(self,case_list)
    coon.commit()
    cursor.close()
    coon.close()
    print("driver.quit()")
    self.driver.quit()

@app.task    
def appauto_testcase2(self):            #流程 的 相关接口
    print("appauto_testcase2")
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = 'emulator-5554'
#   desired_caps['appPackage'] = 'com.android.calculator2'
#   desired_caps['appActivity'] = '.Calculator'
    desired_caps['app'] = PATH('csdn.apk')
    time.sleep(1)
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(1)
    sql="SELECT id,appfindmethod,appevelement,appoptmethod,appassertdata,`apptestresult` from apptest_appcasestep where apptest_appcasestep.Appcase_id=2 ORDER BY id ASC " 
    coon = pymysql.connect(user='qa',passwd='qatest',db='autotest',port=3306,host='127.0.0.1',charset='utf8')
    cursor = coon.cursor()
    aa=cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:   
        case_list = []
        case_list.append(ii)
        apptestcase(self,case_list)
    coon.commit()
    cursor.close()
    coon.close()
    self.driver.quit()

def apptestcase(self,case_list):
    for case in case_list:
        try:   
            case_id = case[0]
            findmethod = case[1] 
            evelement = case[2]
            optmethod = case[3]
        except Exception as e:
            return '测试用例格式不正确！%s'%e
        time.sleep(10)

        if optmethod== 'click' and findmethod=='find_element_by_id':
            print("查找元素->%s,操作方法->%s"%(evelement,optmethod))
            self.driver.find_element_by_id(evelement).click()
        elif optmethod== 'click' and findmethod=='find_element_by_name':
            print("查找元素->%s,操作方法->%s"%(evelement,optmethod))
            self.driver.find_element_by_name(evelement).click()
        elif optmethod=='sendkey':
            print("查找元素->%s,操作方法->%s"%(evelement,optmethod))
            self.driver.find_element_by_name(evelement).send_keys()
