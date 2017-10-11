# -*- coding: UTF-8 -*-
import json

__author__ = "xdg"

import csv
import numpy as np
import os
import pandas as pd
from random import shuffle
import time
import datetime

#找文件下的文件
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print root
        # print(dirs)
        new_files=files
    return new_files

#数据存放路径
filepath='G:/Git/304first/data/users/'

print ("开始处理...")

#得到user文件夹下的所有文件名
filenames=file_name(filepath)
#print filenames

all_User={}#所有用户的所有购买日期
all_user_interval={}#所有用户购买日期间隔
count=1 #第几个用户
for filename in filenames:
    username=filename[:-4] #去掉.csv后缀
    #print ('第%d个用户'%count)
    df=pd.read_csv(filepath+filename,header=None)#不加header=None则会把第一行数据当做header，这样会少读一行数据
    #单独用户的矩阵
    matrix = df.as_matrix()
    #print matrix.shape
    #统计每个用户所有消费日期
    userdate=list(set(matrix[:,8]))
    if username not in all_User.keys():
        all_User.keys().append(username)
        all_User[username] = userdate
    else:
        all_User[username] = userdate

    #统计每个用户所有消费日期
    userdate.sort()#按日期大小排序
    userdate_interval=[0]
    for i in range(len(userdate)):
        if i+1==len(userdate):
            break
        #提取出年月日，如20150201
        year1 = long(str(userdate[i])[:4])  # 例如2015
        mon1 = long(str(userdate[i])[4:6])  # 例如02
        day1 = long(str(userdate[i])[-2:])  # 例如01

        year2 = long(str(userdate[i+1])[:4])  # 例如2015
        mon2 = long(str(userdate[i+1])[4:6])  # 例如02
        day2 = long(str(userdate[i+1])[-2:])  # 例如01

        #相邻日期相减得到相差的天数
        d1=datetime.date(year1,mon1,day1)
        d2=datetime.date(year2,mon2,day2)
        interval=(d2-d1).days
        userdate_interval.append(interval)  #单个用户购买日期间隔集合

    if username not in all_user_interval.keys():
        all_user_interval.keys().append(username)
        all_user_interval[username] = userdate_interval
    else:
        all_User[username] = userdate_interval
    #count+=1

print ("处理结束...")
# print all_User
# print all_user_interval


print("将结果字典存为json格式...")
#所有用户消费日期（存起来，跑模型会用）
with open(os.path.join("G:/Git/304first/data/", 'user_purchase_date.json'), 'w') as f:
    json.dump(all_User, f)
#所有用户消费日期间隔（存起来，跑模型会用）
with open(os.path.join("G:/Git/304first/data/", 'user_purchase_date_interval.json'), 'w') as f:
    json.dump(all_user_interval, f)
