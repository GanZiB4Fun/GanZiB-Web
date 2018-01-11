#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 15:12
# @Author  : GanZiB
# @Email   : ganzib4fun@163.com
# @Site    : 
# @File    : consts.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HOSTNAME = '127.0.0.1'
DATABASE = 'r'
# 家
USERNAME = 'root'
PASSWORD = 'root'
# 公司
# USERNAME = 'web'
# PASSWORD = 'web'
# 阿里云
# USERNAME = 'root'
# PASSWORD = 'ganzib'

DB_URI = 'mysql://{}:{}@{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, DATABASE)

eng = create_engine(DB_URI, connect_args={'charset': 'utf8'})
Session = sessionmaker(bind=eng)
session = Session()
