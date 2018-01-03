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

HOSTNAME = 'localhost'
DATABASE = 'r'
# USERNAME = 'root'
USERNAME = 'web'
# PASSWORD = 'root'
PASSWORD = 'web'
DB_URI = 'mysql://{}:{}@{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, DATABASE)

eng = create_engine(DB_URI, connect_args={'charset': 'utf8'})
Session = sessionmaker(bind=eng)
session = Session()
