#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 下午10:15
# @Author  : ChengLu
# @File    : run.py
# @Contact : 2854859592@qq.com
from scrapy import cmdline


name = 'ship'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
