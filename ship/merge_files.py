#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 下午3:01
# @Author  : ChengLu
# @File    : merge_files.py
# @Contact : 2854859592@qq.com
import os
import sys


def merge_files(src_dir, des_filename):
    file_list = os.listdir(src_dir)
    with open(des_filename, "a+", encoding='utf-8') as des:
        for file in file_list:
            with open(os.path.join(src_dir, file)) as src:
                content = src.read()
                des.write(content)


if __name__ == '__main__':
    src = str(sys.argv[1])  # 获取path参数
    des = str(sys.argv[2])
    merge_files(src, des)
