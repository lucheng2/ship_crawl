#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 下午2:42
# @Author  : ChengLu
# @File    : json2csv.py
# @Contact : 2854859592@qq.com

import codecs
# -*-coding:utf-8-*-
import csv
import json


def trans(path):
    jsonData = codecs.open(path + '.json', 'r', 'utf-8')
    # csvfile = open(path+'.csv', 'w') # 此处这样写会导致写出来的文件会有空行
    # csvfile = open(path+'.csv', 'wb') # python2下
    # csvfile = open(path + '.csv', 'w', newline='')  # python3下
    csvfile = codecs.open(path + '.csv', 'w', 'utf_8_sig')  #解决写入csv时中文乱码
    writer = csv.writer(csvfile)
    keys = ['Name', 'Flag', 'MMSI', 'IMO', 'Call_Sign', 'Type', 'Size',
            'Speed_AVG_or_MAX', 'Draught_AVG', 'GRT', 'DWT', 'Owner', 'Build']
    writer.writerow(keys)

    for dic in jsonData:
        dic = json.loads(dic[0:-1])
        writer.writerow(
            [' '.join(dic['Name']), ' '.join(dic['Flag']), ' '.join(dic['MMSI']), ' '.join(dic['IMO']),
             ' '.join(dic['Call_Sign']), ' '.join(dic['Type']), ' '.join(dic['Size']),
             ' '.join(dic['Speed_AVG_or_MAX']), ' '.join(dic['Draught_AVG']), ' '.join(dic['GRT']), ' '.join(dic['DWT']),
             ' '.join(dic['Owner']), ' '.join(dic['Build']),
             ])
    jsonData.close()
    csvfile.close()


if __name__ == '__main__':
    # path = str(sys.argv[1])  # 获取path参数
    path = "./ship_info"
    print(path)
    trans(path)
