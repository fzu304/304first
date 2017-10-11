# -*- coding: UTF-8 -*-
__author__ = "xdg"

import csv
import numpy as np
import os
import pandas as pd
from random import shuffle
import time

#找文件下的文件
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print root
        # print(dirs)
        new_files=files
    return new_files
#获取列表最小值
def getmin(a=[]):
    min=a[0]
    for i in range(len(a)):
        if a[i]<min:
            min=a[i]
    return min


filepath='G:/Git/304first/data/users/'
#得到user文件夹下的所有文件名
filenames=file_name(filepath)

all_User={}#所有用户的每个月份第一次购买日期
count=1 #第几个用户
for filename in filenames:
    username=filename[:-4]
    #print ('第%d个用户'%count)
    df=pd.read_csv(filepath+filename,header=None)#不加header=None则会把第一行数据当做header，这样会少读一行数据
    #单独用户的矩阵
    matrix = df.as_matrix()
    #print matrix.shape
    #统计每个用户每个月第一次消费的日期
    user_date=[]

    for i in range(12):
        tempdate = []
        for row in matrix:
            mindate = min(matrix[:, 8])  #
            if i+1 == int(str(row[9])[4:]):
                tempdate.append([i+1,str(row[8])[6:]])
        if len(tempdate)>0:
            #user_date.append([tempdate[0][0], getmin(np.array(tempdate)[:, 1])])
            user_date.append( getmin(np.array(tempdate)[:, 1]))
        else:
            user_date.append("00")

    if username not in all_User.keys():
        all_User.keys().append(username)
        all_User[username] = user_date
    else:
        all_User[username] = user_date
    #count += 1


#all_User存放所有用户每个月第一次购买日期
df_date=pd.DataFrame(all_User,index=["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"],columns=all_User.keys())
print df_date

print ("将结果存为csv文件...")
df_date.to_csv("G:/Git/304first/data/user_first_purchase_date.csv")
print("保存结束！")