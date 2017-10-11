# -*- coding: UTF-8 -*-
__author__ = "xdg"

import csv
import numpy as np
import os
import pandas as pd
from random import shuffle
import time

print ("开始处理...")
start_time=time.time()#记录开始时间

#读取csv文件，得到矩阵
df=pd.read_excel("G:/Git/304first/data/data1.xlsx")
data_matrix=df.as_matrix()
data_matrix=np.array(data_matrix)

#获取矩阵第一列（用户名列表）
userlist=data_matrix[:,1]
#获取用户名集合（无重复）
userset=list(set(userlist))

print ("用户：")
print (userset)
#分离出每个用户数据，单独存储


#方法1
#count=1
# for row in data_matrix:
#     print ("处理第%d行"% count)
#     for user in userset:
#         if str(row[1])== str(user):
#             with open("G:/Git/304first/data/users/"+str(user)+".csv","a") as f:
#                 csvwriter=csv.writer(f)
#                 csvwriter.writerow(row)
#     count+=1

#方法2
userNum=1  #用户个数
total_dataNum=0 #所有记录数
for user in userset:
    print (("第%d个用户"%userNum+user))
    user_mat=[]
    data_count=0#每个用户消费记录条数
    for row in data_matrix:
        if str(row[1])== str(user):
            user_mat.append(row)
            data_count+=1
    (pd.DataFrame(user_mat)).to_csv("G:/Git/304first/data/users/"+str(user)+".csv",index=False,header=False,encoding="UTF-8")#如果需要加上头，则删掉index和header参数
    print ("此用户有%d条消费记录"%data_count)
    total_dataNum+=data_count
    userNum+=1

print ("处理完毕！")
end_time=time.time()  #记录结束时间
print ('用时：',end_time-start_time)

print ("\n表中共有%d条数据"%total_dataNum)
print ("共有%d个用户"%len(userset))





