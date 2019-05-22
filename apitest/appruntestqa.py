# -*- coding:utf-8 -*-
#####################################
#作者：fin
#日期：2019年1月
#版本：autotestplat V1.1
#####################################
import  os
import time as t
from appium import webdriver
import pymysql


def appauto_testcase():            #app例
    print("appauto_testcase")
    # 读取设备 id
    read_DeviceId = list( os.popen( 'adb devices' ).readlines() )
        # 读取设备系统版本号
    device_Android_Version = list( os.popen( 'adb shell getprop ro.build.version.release' ).readlines() )
    print ("device_Android_Version",device_Android_Version)
    device_Id = read_DeviceId[1].split( '\t' )[0]
    print ("device_Id",device_Id)


    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = 'CSX4C17829000398'
    desired_caps['appPackage'] = 'com.android.calculator2'
    desired_caps['appActivity'] = '.Calculator'
    t.sleep(3)
    print("before Remote")
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    print("Remote is ok!")
    t.sleep(3)
    sql="SELECT id,appfindmethod,appevelement,appoptmethod,appassertdata,`apptestresult` from apptest_appcasestep where apptest_appcasestep.Appcase_id=1 ORDER BY id ASC " 
    coon = pymysql.connect(user='qa',passwd='qatest',db='autotest',port=3306,host='127.0.0.1',charset='utf8')
    cursor = coon.cursor()
    aa=cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:   
        case_list = []
        case_list.append(ii)
        apptestcase(driver,case_list)
    coon.commit()
    cursor.close()
    coon.close()
    driver.quit()



def apptestcase(dr,case_list):
    print("case_list",case_list)
    for case in case_list:
        try:   
            case_id = case[0]
            findmethod = case[1] 
            evelement = case[2]
            optmethod = case[3]
        except Exception as e:
            return '测试用例格式不正确！%s'%e
        t.sleep(10)
        dr.find_element_by_id("com.android.calculator2:id/digit_1").click()
        dr.find_element_by_id("com.android.calculator2:id/op_add").click()
        dr.find_element_by_id("com.android.calculator2:id/digit_2").click()
        dr.find_element_by_id("com.android.calculator2:id/eq").click()


if __name__ == "__main__":
    appauto_testcase()