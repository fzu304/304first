# -*- coding: UTF-8 -*-
__author__ = "xdg"
'''
将每个大类和中类每天的销量进行统计，保存在csv中，
与获取所有类别日销量v1.py不同的是，将没有销售的日期，销售量设置为0，每个类别都有120条数据（31+28+31+30）
'''

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

#数据存放路径
filepath='G:/Git/304first/data/BigClass/'
filepath2='G:/Git/304first/data/MidClass/'


#得到大类BigClass文件夹下的所有类文件名
filenames1=file_name(filepath)
#得到中类MidClass文件夹下的所有类文件名
filenames2=file_name(filepath2)

BigClassSaleData=[]#大类日销量数组
MidClassSaleData=[]#中类日销量数组
daysinMonth={"01":31,"02":28,"03":31,"04":30} #每个月的天数
print("处理大类")


def DataProcess(filepath="",filenames=[],classNum=1):
    targetPath="G:/Git/304first/data/DateData/Big/"
    targetPath2 = "G:/Git/304first/data/DateData/Mid/"
    if classNum==1:
        print ("开始处理大类...")
    else:
        print("开始处理中类...")
    for file in filenames:
        BigClassSaleData = []  # 大类日销量数组
        classdf = pd.read_csv(filepath+file, header=None, index_col=None, encoding="UTF-8")
        classdf=classdf.as_matrix();
        allData=[]
        for days in daysinMonth:  #月份键
            #count=0
            Mondata = [data for data in classdf if data[8] == int("2015" + days)]  #201501  整个月的数据
            #每一天
            dateData = []
            for i in range(daysinMonth[days]):
                if i+1>9:
                    date="2015"+days+str(i+1) #两位数   如20150211
                else:
                    date="2015"+days+"0"+str(i+1) #个位数   如20150204
                count=0
                for row in Mondata:
                    if int(str(row[7])[-2:])==i+1:  #日期从1开始
                        count+=1
                dateData.append([int(date),count])
            allData.extend(dateData)

        # print ("此类别1月到4月的日销量为",allData)
        # print ("####################################")
        dateDatadf=pd.DataFrame(allData,columns=["日期","销量"],index=None)
        dateDatadf.sort_values(by="日期",inplace=True) #inpalce=True 参数表示将更改应用到df上，否则不会保存
        if(classNum==1):
            dateDatadf.to_csv(targetPath+file,index=False,encoding="UTF-8")
        else:
            dateDatadf.to_csv(targetPath2 + file,index=False, encoding="UTF-8")
    print ("处理完毕！")

if __name__=="__main__":
    DataProcess(filepath,filenames1,1)
    DataProcess(filepath2,filenames2,2)




